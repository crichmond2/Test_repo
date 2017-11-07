$(function() {
  var scheme = window.location.protocol == "https:" ? "wss" : "ws";
  var chatsock = new ReconnectingWebSocket(scheme + '://' + window.location.host + "/chat" + window.location.pathname);

  chatsock.onmessage = function(message){
    console.log("clicked")
    var data = JSON.parse(message.data);
    var chat = $("#chat")
    var ele = $('<tr></tr>')
    ele.append($("<td>></td>").text(data.timestamp))
    ele.append($("<td>></td>").text(data.handle))
    ele.append($("<td>></td>").text(data.message))
    chat.append(ele)
      
  };

  $("#chatform").on("submit",function(event) {
    var message = {
      handle:document.getElementById('username').innerHTML,//$('#handle').val(),
      message: $('#message').val(),
      }
      console.log(message)
      chatsock.send(JSON.stringify(message));
      $("#message").val('').focus();
      return false;
  });
});
