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
jQuery(document).ready(function($){
    // browser window scroll (in pixels) after which the "back to top" link is shown
    var offset = 100,
        //browser window scroll (in pixels) after which the "back to top" link opacity is reduced
        offset_opacity = 1200,
        //duration of the top scrolling animation (in ms)
        scroll_top_duration = 700,
        //grab the "back to top" link
        $back_to_top = $('.top');
    //hide or show the "back to top" link
    $(window).scroll(function(){
        ( $(this).scrollTop() > offset ) ? $back_to_top.addClass('is-visible') : $back_to_top.removeClass('is-visible fade-out');
        if( $(this).scrollTop() > offset_opacity ) { 
            $back_to_top.addClass('fade-out');
        }
    });
    //smooth scroll to top
    $back_to_top.on('click', function(event){
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0 ,
            }, scroll_top_duration
        );
    });

});