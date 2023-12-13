#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let i = list.length - 1;
  for (let n = 0; n < list.length; n++) {
    newList[n] = list[i];
    i--;
  }
  return newList;
};
