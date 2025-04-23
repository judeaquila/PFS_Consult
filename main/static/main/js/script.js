// Wait for the DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function() {

    // Scroll Animations - Add 'animated' class to elements when they are in the viewport
    const scrollElements = document.querySelectorAll('[data-animate]');
    
    const inView = (element) => {
      const rect = element.getBoundingClientRect();
      return rect.top <= window.innerHeight && rect.bottom >= 0;
    };
  
    const handleScrollAnimations = () => {
      scrollElements.forEach((element) => {
        if (inView(element)) {
          element.classList.add('animated');
        }
      });
    };
  
    // Initialize scroll animations
    handleScrollAnimations();
    window.addEventListener('scroll', handleScrollAnimations);
  
    // Navbar Toggle for mobile view
    const navbarToggle = document.querySelector('.navbar-toggler');
    const navbarCollapse = document.querySelector('.navbar-collapse');
    
    if (navbarToggle && navbarCollapse) {
      navbarToggle.addEventListener('click', function() {
        navbarCollapse.classList.toggle('collapse');
      });
    }
  
    // Sidebar toggle for mobile view
    const sidebarToggle = document.querySelector('.sidebar-toggler');
    const sidebar = document.querySelector('.sidebar');
    
    if (sidebarToggle && sidebar) {
      sidebarToggle.addEventListener('click', function() {
        sidebar.classList.toggle('show');
        sidebar.classList.toggle('collapsed');
      });
    }
  
    // Collapsible sidebar automatically collapsing on mobile, still with option to expand
    const mediaQuery = window.matchMedia('(max-width: 767px)');
    const collapseSidebar = () => {
      if (mediaQuery.matches) {
        sidebar.classList.add('collapsed');
      } else {
        sidebar.classList.remove('collapsed');
      }
    };
  
    // Add event listener for resizing window
    mediaQuery.addEventListener('change', collapseSidebar);
    collapseSidebar();
  
    // Button Hover Effect
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach((btn) => {
      btn.addEventListener('mouseover', function() {
        btn.style.backgroundColor = '#000';
        btn.style.color = '#fff';
      });
  
      btn.addEventListener('mouseout', function() {
        btn.style.backgroundColor = '';
        btn.style.color = '';
      });
    });
  
    // Clickable cards - add event listener to all cards with 'clickable-card' class
    const clickableCards = document.querySelectorAll('.clickable-card');
    
    clickableCards.forEach((card) => {
      card.addEventListener('click', function() {
        // Optionally, you can redirect to a detail page or open a modal
        window.location.href = card.dataset.href || '#'; // Uses 'data-href' for redirection
      });
    });
  
    // Notifications dropdown toggle
    const notificationDropdown = document.querySelector('.notifications-dropdown');
    if (notificationDropdown) {
      notificationDropdown.addEventListener('click', function() {
        this.classList.toggle('show');
      });
    }
  
  });

  // Login Page Animations
  // Toggle Password View
  const togglePassword = document.querySelector(".toggle-password");
    const passwordInput = document.getElementById("password");

    togglePassword.addEventListener("click", function() {
      const type = passwordInput.getAttribute("type") === "password" ? "text" : "password";
      passwordInput.setAttribute("type", type);
      this.classList.toggle("bi-eye");
      this.classList.toggle("bi-eye-slash");
  });