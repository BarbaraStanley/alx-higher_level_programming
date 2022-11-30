#!/usr/bin/node
exports.converter = function (base) {
  return function (basenum) {
    return basenum.toString(base);
  };
};
