function scheduleAnkiReview() {
  // Generate random hour between 12-23 (noon to 11pm) in Taipei time
  const randomHour = Math.floor(Math.random() * 12) + 12;
  const randomMinute = Math.floor(Math.random() * 60);

  // Format times for display and cron syntax
  const formattedTime = `${randomHour}:${randomMinute
    .toString()
    .padStart(2, "0")}`;

  // Convert from Taipei time (UTC+8) to UTC for GitHub Actions
  let utcHour = randomHour - 8;
  if (utcHour < 0) utcHour += 24;

  // Cron syntax for GitHub Actions (minute hour * * *)
  const cronExpression = `${randomMinute} ${utcHour} * * *`;

  console.log(
    `Generated random time: ${formattedTime} Taipei time (${cronExpression} UTC)`
  );

  // GitHub repository details
  const owner = "HsiaoSeanHS";
  const repo = "VisualStudioCode";
  const workflow_id = "anki_review.yml";
  const githubToken =
    PropertiesService.getScriptProperties().getProperty("GITHUB_TOKEN");

  // Option 1: Update the workflow file directly with new cron schedule
  updateWorkflowFile(owner, repo, workflow_id, cronExpression, githubToken);

  // Option 2: Trigger repository_dispatch event
  triggerRepositoryDispatch(owner, repo, githubToken, formattedTime);

  // Record the scheduled time
  const now = new Date();
  const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  sheet.appendRow([
    now,
    formattedTime,
    `UTC: ${utcHour}:${randomMinute.toString().padStart(2, "0")}`,
  ]);
}

function updateWorkflowFile(owner, repo, workflow_id, cronExpression, token) {
  try {
    // First, get the current workflow file
    const getUrl = `https://api.github.com/repos/${owner}/${repo}/contents/.github/workflows/${workflow_id}`;
    const getOptions = {
      headers: {
        Authorization: `token ${token}`,
        Accept: "application/vnd.github.v3+json",
      },
      muteHttpExceptions: true,
    };

    const getResponse = UrlFetchApp.fetch(getUrl, getOptions);
    const fileData = JSON.parse(getResponse.getContentText());
    const content = Utilities.base64Decode(fileData.content);
    const contentStr = Utilities.newBlob(content).getDataAsString();

    // Update the cron expression in the workflow file
    const updatedContent = contentStr.replace(
      /cron: '([0-9* ]+)'/,
      `cron: '${cronExpression}'`
    );

    // Commit the updated file back to GitHub
    const updateUrl = `https://api.github.com/repos/${owner}/${repo}/contents/.github/workflows/${workflow_id}`;
    const updateOptions = {
      method: "put",
      headers: {
        Authorization: `token ${token}`,
        Accept: "application/vnd.github.v3+json",
      },
      payload: JSON.stringify({
        message: `Update scheduled time to ${cronExpression}`,
        content: Utilities.base64Encode(updatedContent),
        sha: fileData.sha,
      }),
      muteHttpExceptions: true,
    };

    const updateResponse = UrlFetchApp.fetch(updateUrl, updateOptions);
    console.log("Workflow file updated:", updateResponse.getContentText());
    return true;
  } catch (error) {
    console.error("Error updating workflow file:", error);
    return false;
  }
}

function triggerRepositoryDispatch(owner, repo, token, scheduledTime) {
  try {
    const url = `https://api.github.com/repos/${owner}/${repo}/dispatches`;
    const options = {
      method: "post",
      headers: {
        Authorization: `token ${token}`,
        Accept: "application/vnd.github.v3+json",
      },
      payload: JSON.stringify({
        event_type: "schedule_anki_review",
        client_payload: {
          scheduled_time: scheduledTime,
        },
      }),
      muteHttpExceptions: true,
    };

    const response = UrlFetchApp.fetch(url, options);
    console.log("Repository dispatch triggered:", response.getResponseCode());
    return true;
  } catch (error) {
    console.error("Error triggering repository dispatch:", error);
    return false;
  }
}
