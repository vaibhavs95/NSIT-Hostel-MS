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
	// handle links with @href started with '#' only
	$(document).on('click', 'a[href^="#"]', function(e) {
		// target element id
		var id = $(this).attr('href');
	
		// target element
		var $id = $(id);
		if ($id.length === 0) {
			return;
		}
	
		// prevent standard hash navigation (avoid blinking in IE)
		e.preventDefault();
	
		// top position relative to the document
		var pos = $(id).offset().top;
	
		// animated top scrolling
		$('body, html').animate({scrollTop: pos},1000);
	});
}
