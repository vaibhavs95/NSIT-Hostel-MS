function main() {
	$('.button-collapse').sideNav();
	$('.modal-trigger').leanModal();
	$('.datepicker').pickadate({
		selectMonths: true,
		selectYears: 200 
	});
	$(".login-button").click(function () {
		$('.button-collapse').sideNav('hide');
	});
	$("#forgot-button").click(function () {
		$('#login-modal').closeModal();
	});
	$("#flogin-button").click(function () {
		$('#forgot-password').closeModal();
		$('#login-modal').openModal();
	});
	
	$("#lin1").click(function(){
		$("#main").css("display","block");
		$("#mess").css("display","none");
		$("#eventlist").css("display","none");
		$("#facilities").css("display","none");
	});
	$("#lin2").click(function(){
		$("#notice").css("display","block");
		$("#mess").css("display","none");
		$("#eventlist").css("display","none");
		$("#facilities").css("display","none");
	});
	$("#lin3").click(function(){
		$("#forms").css("display","block");
		$("#mess").css("display","none");
		$("#eventlist").css("display","none");
		$("#facilities").css("display","none");
	});
	$("#lin4").click(function(){
		$("#mess").css("display","block");
		$("#main").css("display","none");
		$("#notice").css("display","none");
		$("#forms").css("display","none");
	});
	$("#lin5").click(function(){
		$("#eventlist").css("display","block");
		$("#main").css("display","none");
		$("#notice").css("display","none");
		$("#forms").css("display","none");
	});
	$("#lin6").click(function(){
		$("#facilities").css("display","block");
		$("#main").css("display","none");
		$("#notice").css("display","none");
		$("#forms").css("display","none");
	});
	
	// handle links with @href started with '#' only
	// $(document).on('click', 'a[href^="#"]', function(e) {
	//	// target element id
	//	var id = $(this).attr('href');
	//
	//	// target element
	//	var $id = $(id);
	//	if ($id.length === 0) {
	//		return;
	//	}
	//
	//	// prevent standard hash navigation (avoid blinking in IE)
	//	e.preventDefault();
	//
	//	// top position relative to the document
	//	var pos = $(id).offset().top;
	//
	//	// animated top scrolling
	//	$('body, html').animate({scrollTop: pos},1000);
	//});
	
	//	$( "#tabs" ).tabs();
	
}
