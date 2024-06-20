#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length - 1;
  const revlist = [];
  for (let i = 0; i < list.length; i++) {
    revlist[i] = list[len - i];
  }
  return revlist;
};
