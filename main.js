/**
 * Nexlamp Technology - Main JavaScript
 * Mobile-first, accessible, vanilla JS
 */

(function() {
    'use strict';

    // ========================================
    // Mobile Navigation Toggle
    // ========================================
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.getElementById('nav-menu');

    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            const isExpanded = this.getAttribute('aria-expanded') === 'true';
            this.setAttribute('aria-expanded', !isExpanded);
            navMenu.classList.toggle('active');
            document.body.style.overflow = !isExpanded ? 'hidden' : '';
        });

        // Close menu when clicking on a link
        navMenu.querySelectorAll('a').forEach(function(link) {
            link.addEventListener('click', function() {
                navToggle.setAttribute('aria-expanded', 'false');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
            });
        });

        // Close menu on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && navMenu.classList.contains('active')) {
                navToggle.setAttribute('aria-expanded', 'false');
                navMenu.classList.remove('active');
                document.body.style.overflow = '';
                navToggle.focus();
            }
        });
    }

    // ========================================
    // Smooth Scroll for Anchor Links
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
                // Update URL without jumping
                history.pushState(null, '', targetId);
            }
        });
    });

    // ========================================
    // Lazy Loading Images (Native + Fallback)
    // ========================================
    if ('loading' in HTMLImageElement.prototype) {
        // Browser supports native lazy loading
        document.querySelectorAll('img[data-src]').forEach(function(img) {
            img.src = img.dataset.src;
            img.removeAttribute('data-src');
        });
    } else {
        // Fallback for older browsers
        const imageObserver = new IntersectionObserver(function(entries, observer) {
            entries.forEach(function(entry) {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    if (img.dataset.src) {
                        img.src = img.dataset.src;
                        img.removeAttribute('data-src');
                    }
                    observer.unobserve(img);
                }
            });
        }, {
            rootMargin: '50px 0px'
        });

        document.querySelectorAll('img[data-src]').forEach(function(img) {
            imageObserver.observe(img);
        });
    }

    // ========================================
    // Table of Contents Active State
    // ========================================
    const toc = document.querySelector('.toc');
    if (toc) {
        const headings = document.querySelectorAll('.article-content h2, .article-content h3');
        const tocLinks = toc.querySelectorAll('a');

        if (headings.length > 0 && tocLinks.length > 0) {
            const headingObserver = new IntersectionObserver(function(entries) {
                entries.forEach(function(entry) {
                    if (entry.isIntersecting) {
                        const id = entry.target.id;
                        tocLinks.forEach(function(link) {
                            link.classList.remove('active');
                            if (link.getAttribute('href') === '#' + id) {
                                link.classList.add('active');
                            }
                        });
                    }
                });
            }, {
                rootMargin: '-80px 0px -60% 0px'
            });

            headings.forEach(function(heading) {
                headingObserver.observe(heading);
            });
        }
    }

    // ========================================
    // Blog Category Filter
    // ========================================
    const categoryLinks = document.querySelectorAll('.category-list a[data-filter]');
    const blogPosts = document.querySelectorAll('.blog-post-item');

    categoryLinks.forEach(function(link) {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const filter = this.dataset.filter;

            // Update active state
            categoryLinks.forEach(function(l) {
                l.style.fontWeight = '';
                l.style.color = '';
            });
            this.style.fontWeight = '600';
            this.style.color = 'var(--primary)';

            // Filter posts
            blogPosts.forEach(function(post) {
                if (filter === 'all' || post.dataset.category === filter) {
                    post.style.display = '';
                    post.style.animation = 'fadeIn 0.3s ease';
                } else {
                    post.style.display = 'none';
                }
            });
        });
    });

    // ========================================
    // Scroll-based Header Shadow
    // ========================================
    const header = document.querySelector('.site-header');
    let lastScroll = 0;

    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 10) {
            header.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
        } else {
            header.style.boxShadow = '';
        }
        
        lastScroll = currentScroll;
    });

    // ========================================
    // Performance: Preload Critical Resources
    // ========================================
    function preloadResource(href, as, type) {
        const link = document.createElement('link');
        link.rel = 'preload';
        link.href = href;
        link.as = as;
        if (type) link.type = type;
        document.head.appendChild(link);
    }

    // Preload next page if on blog listing
    if (document.querySelector('.pagination')) {
        const nextLink = document.querySelector('.page-next');
        if (nextLink) {
            preloadResource(nextLink.href, 'document');
        }
    }

    // ========================================
    // Analytics Helper (Placeholder)
    // ========================================
    function trackEvent(eventName, properties) {
        // Placeholder for analytics tracking
        // Example: gtag('event', eventName, properties);
        if (window.console && console.debug) {
            console.debug('Track:', eventName, properties);
        }
    }

    // Track CTA clicks
    document.querySelectorAll('.btn-primary').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const text = this.textContent.trim();
            trackEvent('cta_click', { button_text: text });
        });
    });

    // ========================================
    // Service Worker Registration (PWA Ready)
    // ========================================
    if ('serviceWorker' in navigator) {
        window.addEventListener('load', function() {
            // Uncomment when service worker is available
            // navigator.serviceWorker.register('/sw.js');
        });
    }

})();

// ========================================
// CSS Animation Keyframes (injected)
// ========================================
const style = document.createElement('style');
style.textContent = `
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
`;
document.head.appendChild(style);
