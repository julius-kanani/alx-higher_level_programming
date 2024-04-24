#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, { json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Unexpected status code:', response.statusCode);
    return;
  }

  const completedTasks = {};

  body.forEach(task => {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });
  console.log(completedTasks);
});
