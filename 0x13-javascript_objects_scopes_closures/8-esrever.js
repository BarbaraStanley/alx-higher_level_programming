#!/usr/bin/node
exports.esrever = function (list) {
  let rev = [];
  let a = 0;
  for (let i = list.length - 1; i >= 0; i--) {
    rev[a] = list[i];
    a = a + 1;
  }
  return rev;
}
