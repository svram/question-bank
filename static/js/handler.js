var showingAnswer = false;
var colors = ['#16a085', '#27ae60', '#2c3e50', '#f39c12', '#e74c3c', 
'#9b59b6', '#FB6964', '#342224', "#472E32", "#BDBB99", "#77B1A9", "#73A857"];

function getRandomColor(){
	return colors[Math.floor(Math.random()*colors.length)];
}

function setupView(){

	//$('#answer').css('display', 'none');
	$('.answerwell').css('opacity', '0.0');
	$('#showButton').text('Show Answer');
	var randColor = getRandomColor();
	$.get( "/random", function(data) {
		$("#question").animate({
			opacity:0
		},500, function(){
			//animation complete
			$("#answer").text(data[1]);
  			$("#question").text(data[0]);
  			
  			$("#question").css('color', randColor);

			$(this).animate({opacity: 1},500, function(){
				
			});

			
		});

		
  		$('.buttontext').animate({opacity:1},500, function(){
  			$(".uibuttons").css("background", randColor);
  			$(this).animate({opacity: 1},500, function(){
				
			});
  		});

  		$('html body').animate({opacity:1},500, function(){
  			$(this).css("background", randColor);
  			$(this).animate({opacity: 1},500, function(){
				
			});
  		});
});

}

$(document).ready(function() {
	setupView();
})


$('#random').click(function(){
	setupView();
});

$('#showButton').click(function(){
	if(!showingAnswer){
		
		$('.answerwell').css('opacity', '1.0');
		$('#showButton').text('Hide Answer');
		showingAnswer = true;
	}
	else{
		
		$('.answerwell').css('opacity', '0.0');
		$('#showButton').text('Show Answer');
		showingAnswer = false;
	}
});