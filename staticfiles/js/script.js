$(window).on("load", function() {
    "use strict";

    //  ============= SIGNIN TAB FUNCTIONALITY =========

    $('.signup-tab ul li').on("click", function(){
        var tab_id = $(this).attr('data-tab');
        $('.signup-tab ul li').removeClass('current');
        $('.dff-tab').removeClass('current');
        $(this).addClass('current animated fadeIn');
        $("#"+tab_id).addClass('current animated fadeIn');
        return false;
    });

    //  ============= SIGNIN SWITCH TAB FUNCTIONALITY =========

    $('.tab-feed ul li').on("click", function(){
        var tab_id = $(this).attr('data-tab');
        $('.tab-feed ul li').removeClass('active');
        $('.product-feed-tab').removeClass('current');
        $(this).addClass('active animated fadeIn');
        $("#"+tab_id).addClass('current animated fadeIn');
        return false;
    });

    //  ============= COVER GAP FUNCTION =========

    var gap = $(".container").offset().left;
    $(".cover-sec > a, .chatbox-list").css({
        "right": gap
    });

    //  ============= OVERVIEW EDIT FUNCTION =========

    $(".overview-open").on("click", function(){
        $("#overview-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#overview-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= EXPERIENCE EDIT FUNCTION =========

    $(".exp-bx-open").on("click", function(){
        $("#experience-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#experience-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= EDUCATION EDIT FUNCTION =========

    $(".ed-box-open").on("click", function(){
        $("#education-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#education-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= LOCATION EDIT FUNCTION =========

    $(".lct-box-open").on("click", function(){
        $("#location-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#location-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= SKILLS EDIT FUNCTION =========

    $(".skills-open").on("click", function(){
        $("#skills-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#skills-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= ESTABLISH EDIT FUNCTION =========

    $(".esp-bx-open").on("click", function(){
        $("#establish-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#establish-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= CREATE PORTFOLIO FUNCTION =========

    $(".gallery_pt > a").on("click", function(){
        $("#create-portfolio").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#create-portfolio").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  ============= EMPLOYEE EDIT FUNCTION =========

    $(".emp-open").on("click", function(){
        $("#total-employes").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#total-employes").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });

    //  =============== Ask a Question Popup ============

    $(".ask-question").on("click", function(){
        $("#question-box").addClass("open");
        $(".wrapper").addClass("overlay");
        return false;
    });
    $(".close-box").on("click", function(){
        $("#question-box").removeClass("open");
        $(".wrapper").removeClass("overlay");
        return false;
    });


    //  ============== ChatBox ============== 


    $(".chat-mg").on("click", function(){
        $(this).next(".conversation-box").toggleClass("active");
        return false;
    });
    $(".close-chat").on("click", function(){
        $(".conversation-box").removeClass("active");
        return false;
    });

    //  ============== ed-opts ==============

    $(".close-ed-opts").on("click", function(){
        $(".ed-options").removeClass("active");
        return false;
    });

    //  ================== Edit Options Function =================


    $(".ed-opts-open").on("click", function(){
        $(this).next(".ed-options").toggleClass("active");
        return false;
    });


    // ============== Menu Script =============

    $(".menu-btn > a").on("click", function(){
        $("nav").toggleClass("active");
        return false;
    });


    //  ============ Notifications Open =============

    $(".not-box-open").on("click", function(){
        $(this).next(".notification-box").toggleClass("active");
    });

    // ============= User Account Setting Open ===========

    $(".user-info").on("click", function(){
        $(this).next(".user-account-settingss").toggleClass("active");
    });

    //  ============= FORUM LINKS MOBILE MENU FUNCTION =========

    $(".forum-links-btn > a").on("click", function(){
        $(".forum-links").toggleClass("active");
        return false;
    });
    $("html").on("click", function(){
        $(".forum-links").removeClass("active");
    });
    $(".forum-links-btn > a, .forum-links").on("click", function(){
        e.stopPropagation();
    });

    // ================ Alert Message ===============

    setTimeout(function(){
      $('#message').fadeOut('slow')
    }, 4000);

    // =============== tags space ======================

    $("#tags").on("click", function(){
        const input = document.getElementById('tags');

        // for not allow space as a first input
        input.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
        });

        // for remove double spaces in between text
        input.addEventListener('keyup', () => {
            input.value = input.value.replace(/  +/g, ' ');
        });

        return false;
    });

    // tags post job
    $("#tags_job").on("click", function(){
        const input = document.getElementById('tags_job');

        // for not allow space as a first input
        input.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
            // prevent tab
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        // for remove double spaces in between text
        input.addEventListener('keyup', (e) => {
            input.value = input.value.replace(/  +/g, ' ');
            // prevent tab
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });

    // tags post project
    $("#tags_project").on("click", function(){
        const input = document.getElementById('tags_project');

        // for not allow space as a first input
        input.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();

            // prevent tab
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        // for remove double spaces in between text
        input.addEventListener('keyup', (e) => {
            input.value = input.value.replace(/  +/g, ' ');

            // prevent tab
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });

    // ==================== hourly_work input =====================

    $("#hourly_work").on("click", function(){
        const hourly_work = document.getElementById('hourly_work');

        hourly_work.onkeydown = function(e) {
            if(!((e.keyCode > 95 && e.keyCode < 106) || (e.keyCode > 47 && e.keyCode < 58) || e.keyCode == 8)) {
                return false;
            }
            // prevent tab
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        return false;
    });

    // ======================= Last_name ===========================

    $("#id_first_name").on("click", function(){
        const first_name = document.getElementById('id_first_name');
        first_name.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent number
            if (keyCode > 47 && keyCode < 58) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent some caracter
            if (keyCode == 188 || keyCode == 189 || keyCode == 187 || keyCode == 191 || keyCode == 221 || keyCode == 186 || keyCode == 219 || keyCode == 226 || keyCode == 190){
                e.preventDefault();
            }

        }
        first_name.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            // prevent number
            if (keyCode > 47 && keyCode < 58) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        return false;
    });

    // =============== Last_name ===============

    $("#id_last_name").on("click", function(){
        const last_name = document.getElementById('id_last_name');
        console.log('test')

        last_name.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent number
            if (keyCode > 47 && keyCode < 58) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }

            // prevent some caracter
            if (keyCode == 188 || keyCode == 189 || keyCode == 187 || keyCode == 191 || keyCode == 221 || keyCode == 186 || keyCode == 219 || keyCode == 226 || keyCode == 190){
                e.preventDefault();
            }
        }

        last_name.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent number
            if (keyCode > 47 && keyCode < 58) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }

        return false;
    });

    // =================== email ===============================

    $("#id_email").on("click", function(){
        const email = document.getElementById('id_email');

        email.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        email.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        return false;
    });

    // =================== phone_number ===============================

    $("#id_phone_number").on("click", function(){
        const phone_number = document.getElementById('id_phone_number');

        phone_number.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        phone_number.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }

        // prevent letters
        phone_number.addEventListener("keypress", function (evt) {
            if (evt.which < 48 || evt.which > 57) {
                evt.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });
        return false;
    });

    // =================== start year ===========================

    $("#id_start_price").on("click", function(){
        const start_price = document.getElementById('id_start_price');

        start_price.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32)
            {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        start_price.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }

        // prevent letters
        start_price.addEventListener("keypress", function (e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (e.which < 48 || e.which > 57){
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });
        return false;
    });

    // ===================  end year ===========================

    $("#id_end_price").on("click", function(){
        const start_price = document.getElementById('id_end_price');

        start_price.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32){
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        start_price.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }

        // prevent letters
        start_price.addEventListener("keypress", function (evt) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (evt.which < 48 || evt.which > 57)
            {
                evt.preventDefault();
            }
            // prevent space
            if (keyCode == 32) {
                evt.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });
        return false;
    });

    // ===================  price job ===========================

    $("#id_price").on("click", function(){
        const start_price = document.getElementById('id_price');

        start_price.onkeydown =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32)
            {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }
        start_price.onkeyup =  function Check(e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        }

        // prevent letters
        start_price.addEventListener("keypress", function (e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (e.which < 48 || e.which > 57){
                e.preventDefault();
            }
            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });
        return false;
    });

    // ===================  location project ===========================

    $("#id_location").on("click", function(){
        const location = document.getElementById('id_location');

        // for not allow space as a first input
        location.addEventListener('keydown', function (e) {
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        // for remove double spaces in between text
        location.addEventListener('keyup', () => {
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            location.value = location.value.replace(/  +/g, ' ');

            // prevent space
            if (keyCode == 32) {
                e.preventDefault();
            }
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });
        return false;
    });

    // ===================  description project ===========================

    $("#id_description_project").on("click", function(){
        const description_project = document.getElementById('id_description_project');

        // for not allow space as a first input
        description_project.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
             var keyCode = (e.keyCode ? e.keyCode : e.which);
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });

    // ===================  description job ===========================

    $("#id_description_job").on("click", function(){
        const description_job = document.getElementById('id_description_job');

        // for not allow space as a first input
        description_job.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });

    // ===================  title project ===========================

    $("#id_name_project").on("click", function(){
        const name_project = document.getElementById('id_name_project');

        // for not allow space as a first input
        name_project.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });

    // ===================  title job ===========================

    $("#id_name_jobs").on("click", function(){
        const name_jobs = document.getElementById('id_name_jobs');

        // for not allow space as a first input
        name_jobs.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });

    // ===================  Category project ===========================

    $("#id_epic_coder").on("click", function(){
        const epic_coder = document.getElementById('id_epic_coder');

        // for not allow space as a first input
        epic_coder.addEventListener('keydown', function (e) {
            if (this.value.length === 0 && e.which === 32) e.preventDefault();
            var keyCode = (e.keyCode ? e.keyCode : e.which);
            // prevent tab
            if (keyCode == 9) {
                e.preventDefault();
            }
        });

        return false;
    });
});