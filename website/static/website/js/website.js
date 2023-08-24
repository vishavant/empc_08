// testimonial slider


function testimonialSlider(){
    const carouselOne = document.getElementById('carouselOne')
    if(carouselOne){
        carouselOne.addEventListener('slid.bs.carousel', function(){
            const activeItem = this.querySelector(".active");
            document.querySelector(".js-testimonial-img").src=
            activeItem.getAttribute("data-js-testimonial-img")
        })
    }

}
testimonialSlider();


$(document).ready(function(){
    /*--Navbar Shrink--*/
    $(window).on("scroll", function(){
        if($(this).scrollTop()>90){
            $(".navbar").addClass("navbar-shrink");
        }
        else{
            $(".navbar").removeClass("navbar-shrink");
        }
    })

    /*--video popup--*/
    const videoSrc = $("#player-1").attr("src");
    $(".video-play-btn, .video-popup").on("click", function(){
        if($(".video-popup").hasClass("open")){
            $(".video-popup").removeClass("open");
            $("#player-1").attr("src", "");
        }
        else{
            $(".video-popup").addClass("open");
            if($("#player-1").attr("src")==''){
             $("#player-1").attr("src", videoSrc);
          }
        }
    });

    /*_________________Features Carousel_________________*/

    $('.features-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                
            },
            600:{
                items:2,
                
            },
            1000:{
                items:3,
            }
        }
    });

    /*_________________Course Carousel_________________*/

    $('.course-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                
            },
            600:{
                items:2,
                
            },
            1000:{
                items:3,
            }
        }
    });    

   /*_________________ testimonial Carousel_________________*/


   $('.testimonials-carousel').owlCarousel({
    loop:true,
    margin:0,
    autoplay:true,
    responsiveClass:true,
    responsive:{
        0:{
            items:1,
            
        },
        600:{
            items:2,
            
        },
        1000:{
            items:3,
        }
    }
});

    /*_________________ Team Carousel_________________*/


    $('.team-carousel').owlCarousel({
        loop:true,
        margin:0,
        autoplay:true,
        responsiveClass:true,
        responsive:{
            0:{
                items:1,
                
            },
            600:{
                items:2,
                
            },
            1000:{
                items:3,
            }
        }
    });
    /*_________________ Page Scrolling _________________*/
    $.scrollIt({
        topOffset: -50
    })
    

/*_________________ navbar collapse _________________*/
$(".nav-link").on("click", function(){
    $(".navbar-collapse").collapse("hide");
});


});