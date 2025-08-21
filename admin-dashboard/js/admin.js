
        // Navigation functionality
        document.addEventListener('DOMContentLoaded', function() {
            const navLinks = document.querySelectorAll('.nav-link[data-page]');
            const appTabs = document.querySelectorAll('.app-tab');
            
            // Handle sidebar navigation
            navLinks.forEach(link => {
                link.addEventListener('click', function(e) {
                    e.preventDefault();
                    
                    // Remove active class from all nav links
                    navLinks.forEach(l => l.classList.remove('active'));
                    
                    // Add active class to clicked link
                    this.classList.add('active');
                    
                    const page = this.getAttribute('data-page');
                    navigateToPage(page);
                });
            });

            // Handle application tabs
            appTabs.forEach(tab => {
                tab.addEventListener('click', function(e) {
                    e.preventDefault();
                    
                    // Remove active class from all tabs
                    appTabs.forEach(t => t.classList.remove('active'));
                    
                    // Add active class to clicked tab
                    this.classList.add('active');
                    
                    // Update statistics based on selected tab
                    updateTabStatistics(this.textContent.trim());
                });
            });

            // Mobile sidebar toggle
            const sidebarToggle = document.createElement('button');
            sidebarToggle.className = 'btn btn-outline-secondary d-md-none me-3';
            sidebarToggle.innerHTML = '<i class="fas fa-bars"></i>';
            sidebarToggle.addEventListener('click', toggleSidebar);
            
            const navbarBrand = document.querySelector('.navbar-brand');
            navbarBrand.parentNode.insertBefore(sidebarToggle, navbarBrand);
        });

        function navigateToPage(page) {
            console.log('Navigating to:', page);
            
            // Show loading state
            showLoading();
            
            // Simulate navigation delay
            setTimeout(() => {
                switch(page) {
                    case 'business-registration':
                        // load business registration page
                        window.location.href = './business-registration/admin-business-registration-home.html';
                        break;

                    case 'product-development':
                        // load product development page
                        window.location.href = './product-development/product-development-home.html';
                        break;  
                    case 'dehydration-services':
                        // load dehydration services page
                        window.location.href = './dehydration-services/admin-dehydration-service-home.html';
                        break;
                    case 'consultation':
                        // load consultation page   
                        window.location.href = './consultation-service/admin-consultation-service-home.html';
                        break;
                    case 'machinery-sourcing':  
                        // load machinery sourcing page
                        window.location.href = './machinery-sourcing/admin-machinery-sourcing-home.html';
                        break;
                    case 'training-audit':
                        // load training and audit page
                        window.location.href = './training&facility-audit/training-facility-audit-home.html';
                        break;  
                    case 'contract-manufacturing':
                        // load contract manufacturing page
                        window.location.href = './contract-manufacturing/contract-manufacturing-home.html';
                        break;

                    case 'packaging-coaching':
                        // load your packaging coaching page  
                        window.location.href = './packaging-service/admin-packaging-service-home.html';
                    case 'fda-food':
                        // load FDA food page
                        window.location.href = './fda-food-herbal/fda-food-herbal.html';
                        break;
                    case 'fda-eateries':
                        // load FDA eateries page
                        window.location.href = './fda-eateries/fda-eateries.html';
                        break;
                        
                    case 'overview':
                        // Stay on current page
                        hideLoading();
                        return;
                    default:
                        alert(`Navigating to ${page}...\n\nIn a real implementation, this would load the respective page.`);
                        break;
                }
                hideLoading();
            }, 500);
        }

        function updateTabStatistics(tabName) {
            // Simulate different statistics for different tabs
            const stats = {
                'Product Development': { total: 9, pending: 5, review: 2, completed: 0, approved: 1, rejected: 1 },
                'Dehydration Services': { total: 6, pending: 3, review: 1, completed: 1, approved: 1, rejected: 0 },
                'Business Registration': { total: 15, pending: 7, review: 3, completed: 2, approved: 2, rejected: 1 },
                'Consultation': { total: 12, pending: 4, review: 2, completed: 3, approved: 2, rejected: 1 },
                'Packaging Consulting': { total: 18, pending: 8, review: 4, completed: 3, approved: 2, rejected: 1 },
                'Machinery Sourcing': { total: 7, pending: 2, review: 1, completed: 2, approved: 1, rejected: 1 },
                'Training & Audits': { total: 10, pending: 4, review: 2, completed: 2, approved: 1, rejected: 1 },
                'Contract Manufacturing': { total: 5, pending: 2, review: 1, completed: 1, approved: 1, rejected: 0 }
            };

            const tabStats = stats[tabName] || stats['Product Development'];
            
            // Update the statistics cards
            const statCards = document.querySelectorAll('.app-stat-number');
            statCards[0].textContent = tabStats.total;
            statCards[1].textContent = tabStats.pending;
            statCards[2].textContent = tabStats.review;
            statCards[3].textContent = tabStats.completed;
            statCards[4].textContent = tabStats.approved;
            statCards[5].textContent = tabStats.rejected;
        }

        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('mobile-open');
        }

        function showLoading() {
            // Create loading overlay
            const loadingOverlay = document.createElement('div');
            loadingOverlay.id = 'loadingOverlay';
            loadingOverlay.style.cssText = `
                position: fixed;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: rgba(255, 255, 255, 0.8);
                display: flex;
                align-items: center;
                justify-content: center;
                z-index: 9999;
            `;
            loadingOverlay.innerHTML = `
                <div class="text-center">
                    <div class="spinner-border text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                    </div>
                    <div class="mt-2 text-muted">Loading page...</div>
                </div>
            `;
            document.body.appendChild(loadingOverlay);
        }

        function hideLoading() {
            const loadingOverlay = document.getElementById('loadingOverlay');
            if (loadingOverlay) {
                loadingOverlay.remove();
            }
        }

        // Real-time updates simulation
        function updateNotifications() {
            const badge = document.querySelector('.notification-badge');
            const bellIcon = document.querySelector('.notification-bell');
            
            // Simulate new notifications
            if (Math.random() > 0.8) {
                badge.style.display = 'block';
                bellIcon.style.animation = 'shake 0.5s ease-in-out';
                
                setTimeout(() => {
                    bellIcon.style.animation = '';
                }, 500);
            }
        }

        // Animate statistics on load
        function animateStats() {
            const statValues = document.querySelectorAll('.stat-value, .app-stat-number');
            
            statValues.forEach(stat => {
                const finalValue = stat.textContent;
                const isNumeric = !isNaN(parseFloat(finalValue.replace(/[^\d.-]/g, '')));
                
                if (isNumeric) {
                    const numericValue = parseFloat(finalValue.replace(/[^\d.-]/g, ''));
                    let currentValue = 0;
                    const increment = numericValue / 30;
                    const prefix = finalValue.replace(/[\d.-]/g, '');
                    
                    stat.textContent = prefix + '0';
                    
                    const timer = setInterval(() => {
                        currentValue += increment;
                        if (currentValue >= numericValue) {
                            currentValue = numericValue;
                            clearInterval(timer);
                        }
                        stat.textContent = prefix + Math.floor(currentValue);
                    }, 50);
                }
            });
        }

        // Initialize animations and updates
        setTimeout(animateStats, 300);
        setInterval(updateNotifications, 15000);

        // Add shake animation for notifications
        const style = document.createElement('style');
        style.textContent = `
            @keyframes shake {
                0%, 100% { transform: translateX(0); }
                25% { transform: translateX(-2px); }
                75% { transform: translateX(2px); }
            }
        `;
        document.head.appendChild(style);
