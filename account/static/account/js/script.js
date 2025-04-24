// Side Bar Toggle
const toggleBtn = document.getElementById('toggleSidebar');
  const sidebar = document.getElementById('sidebar');

  toggleBtn.addEventListener('click', () => {
    sidebar.classList.toggle('show');
  });

  // Ensure sidebar shows on desktop if hidden from mobile toggle
  window.addEventListener('resize', () => {
    if (window.innerWidth > 768) {
      sidebar.classList.remove('show');
    }
  });