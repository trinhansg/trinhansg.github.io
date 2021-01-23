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
	page_size = 8
	start_index = (index - 1)*page_size + 1
	end_index = start_index + page_size
	content = ""
	for(i=start_index;i<end_index;i++){
		content +=
			`<div class="col-sm-6">
				<div class="aspect-ratio-container aspect-ratio-4-3">
					<img src="h${i}.jpg" class="aspect-ratio-object"/>
				</div>			
			</div>`
	}
	$("#content").html(content);
}
var images = [];
function preload_images(num_of_images){
	for (var i = 1; i <= num_of_images; i++) {
        images[i] = new Image();
        images[i].src = "h${i}.jpg";
    }
}