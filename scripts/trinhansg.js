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
	$("#content").load(`page${index}.html`, function() {});
}
function load_page_ex(index){
	content = ""
	for(i=1;i<=8;i++){
		content +=
			`<div class="col-sm-6">
				<div class="aspect-ratio-container aspect-ratio-4-3">
					<img src="page${index}/h${i}.jpg" class="aspect-ratio-object"/>
				</div>			
			</div>`
	}
	$("#content").html(content);
}