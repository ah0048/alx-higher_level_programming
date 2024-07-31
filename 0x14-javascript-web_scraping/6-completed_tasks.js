#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request.get(url, (err, resp, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    const TasksCompleted = tasks.reduce((acc, task) => {
      if (task.completed) {
        acc[task.userId] = (acc[task.userId] || 0) + 1;
      }
      return acc;
    }, {});
    console.log(TasksCompleted);
  }
});
