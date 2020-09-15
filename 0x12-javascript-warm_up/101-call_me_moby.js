#!/usr/bin/node
exports.callMeMoby = function(n, fun) {
  while ((n--)) {
    fun(); 
  }
}
