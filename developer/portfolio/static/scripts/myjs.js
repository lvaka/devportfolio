function scrolly(name){
		console.log('test');
		$('html, body').animate({scrollTop: ($(name).offset().top)},800, "swing");
}

$(document).ready(function () {

	//Grab and style site tech with <em> tags
	var techArray = document.getElementsByClassName('tech')

	for (let x=0;x<techArray.length;x++){
		//splitting csv into an array
		var techLine = techArray[x].innerHTML.split(',');
		techArray[x].innerHTML = ''

		for (let i=0;i<techLine.length;i++){
			techArray[x].innerHTML += '<em>' + techLine[i] + '</em>' 
			
		}
	}
	//End Styling

});

