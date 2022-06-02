
$('document').ready(function() {
  $('#doctorSlideshow').owlCarousel({
    nav: true,
    dots: false,
    navText: ["<span class='mai-arrow-back'></span>", "<span class='mai-arrow-forward'></span>"],
    responsive: {
      0: {
        items: 1
      },
      576: {
        items: 2
      },
      992: {
        items: 3
      }
    }
  });
});

$('document').ready(function() {
  $("a[data-role='smoothscroll']").click(function(e) {
    e.preventDefault();
    
    var position = $($(this).attr("href")).offset().top - nav_height;

    $("body, html").animate({
        scrollTop: position
    }, 1000 );
    return false;
  });
});

$('document').ready(function() {
  // Back to top
  var backTop = $(".back-to-top");

  $(window).scroll(function() {
    if($(document).scrollTop() > 400) {
      backTop.css('visibility', 'visible');
    }
    else if($(document).scrollTop() < 400) {
      backTop.css('visibility', 'hidden');
    }
  });

  backTop.click(function() {
    $('html').animate({
      scrollTop: 0
    }, 1000);
    return false;
  });
});


$('document').ready(function() {
  // Tooltips
  $('[data-toggle="tooltip"]').tooltip();

  // Popovers
  $('[data-toggle="popover"]').popover();

  // Page scroll animate
  new WOW().init();
});


$(document).ready(function() {
  $('#contact_form').bootstrapValidator({
      // To use feedback icons, ensure that you use Bootstrap v3.1.0 or later
      feedbackIcons: {
          valid: 'glyphicon glyphicon-ok',
          invalid: 'glyphicon glyphicon-remove',
          validating: 'glyphicon glyphicon-refresh'
      },
      fields: {
          first_name: {
              validators: {
                      stringLength: {
                      min: 2,
                  },
                      notEmpty: {
                      message: 'Please enter your First Name'
                  }
              }
          },
           last_name: {
              validators: {
                   stringLength: {
                      min: 2,
                  },
                  notEmpty: {
                      message: 'Please enter your Last Name'
                  }
              }
          },
     user_name: {
              validators: {
                   stringLength: {
                      min: 8,
                  },
                  notEmpty: {
                      message: 'Please enter your Username'
                  }
              }
          },
     user_password: {
              validators: {
                   stringLength: {
                      min: 8,
                  },
                  notEmpty: {
                      message: 'Please enter your Password'
                  }
              }
          },
    confirm_password: {
              validators: {
                   stringLength: {
                      min: 8,
                  },
                  notEmpty: {
                      message: 'Please confirm your Password'
                  }
              }
          },
          email: {
              validators: {
                  notEmpty: {
                      message: 'Please enter your Email Address'
                  },
                  emailAddress: {
                      message: 'Please enter a valid Email Address'
                  }
              }
          },
          contact_no: {
              validators: {
                stringLength: {
                      min: 12, 
                      max: 12,
                  notEmpty: {
                      message: 'Please enter your Contact No.'
                   }
              }
          },
     department: {
              validators: {
                  notEmpty: {
                      message: 'Please select your Department/Office'
                  }
              }
          },
              }
          }
      })
      .on('success.form.bv', function(e) {
          $('#success_message').slideDown({ opacity: "show" }, "slow") // Do something ...
              $('#contact_form').data('bootstrapValidator').resetForm();

          // Prevent form submission
          e.preventDefault();

          // Get the form instance
          var $form = $(e.target);

          // Get the BootstrapValidator instance
          var bv = $form.data('bootstrapValidator');

          // Use Ajax to submit form data
          $.post($form.attr('action'), $form.serialize(), function(result) {
              console.log(result);
          }, 'json');
      });
});
