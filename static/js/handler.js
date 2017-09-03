var showingAnswer = false;
var colors = ['#16a085', '#27ae60', '#2c3e50', '#f39c12', '#e74c3c', '#9b59b6', '#FB6964', '#342224', "#472E32", "#BDBB99", "#77B1A9", "#73A857"];

//returns random colors for animating background color change
function getRandomColor() {
	return colors[Math.floor(Math.random() * colors.length)];
}


function setupView() {
	
	//hide answer box and reset 'Show Answer' button text
	$('.answerwell').css('opacity', '0.0');
	$('#showButton').text('Show Answer');


	var randColor = getRandomColor();

	//make ajax GET request to /random to fetch random question and answer
	$.get("/random", function(data) {

		//animate the <p> tag to opacity=0, refer to devtools for visual representation of id's and classes
		$("#question").animate({
			opacity: 0
		}, 500, function() {
			//animation complete
			$("#answer").text(data[1]);
			$("#question").text(data[0]);
			$("#question").css('color', randColor);

			//re-animate back to opacity=1
			$(this).animate({
				opacity: 1
			}, 500, function() {});
		});

		//animate the button text to change its color
		$('.buttontext').animate({
			opacity: 1
		}, 500, function() {
			$(".uibuttons").css("background", randColor);
			$(this).animate({
				opacity: 1
			}, 500, function() {});
		});

		//animate the body color
		$('html body').animate({
			opacity: 1
		}, 500, function() {
			$(this).css("background", randColor);
			$(this).animate({
				opacity: 1
			}, 500, function() {});
		});
	});
}

//setup the view when page loads
$(document).ready(function() {
	setupView();
})

//when random button is clicked, the initial setup function is called
$('#random').click(function() {
	setupView();
});

//when the show answer button is clicked, the bootstrap well with the
//answer is displayed
$('#showButton').click(function() {
	if (!showingAnswer) {
		$('.answerwell').css('opacity', '1.0');
		$('#showButton').text('Hide Answer');
		showingAnswer = true;
	} else {
		$('.answerwell').css('opacity', '0.0');
		$('#showButton').text('Show Answer');
		showingAnswer = false;
	}
});