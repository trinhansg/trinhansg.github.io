$("#content").load("page1.html", function() {
  //alert( "Load was performed." );
});
$("#header").load("https://trinhansg.github.io/header.html", function() {
  //alert( "Load was performed." );
});
$("#footer").load("https://trinhansg.github.io/footer.html", function() {
  //alert( "Load was performed." );
});
function load_page(index){
	$("#content").load("page"+index+".html", function() {
	  //alert( "Load was performed." );
	});
}