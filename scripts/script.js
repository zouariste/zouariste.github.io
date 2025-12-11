/**
 * Portfolio Website - Main JavaScript
 * Author: Mohamed Zouari
 */

(function() {
  'use strict';

  /**
   * Detect platform (Mac, iPhone, iPod, iPad)
   * @returns {boolean} True if Mac-like platform
   */
  const isMacLike = () => {
    return !!navigator.platform.match(/(Mac|iPhone|iPod|iPad)/i);
  };

  /**
   * Get platform class name
   * @returns {string} Platform CSS class
   */
  const getPlatformClassName = () => {
    return isMacLike() ? 'platform-mac' : '';
  };

  /**
   * Toggle mobile navigation menu
   * @param {Event} event - Click event
   */
  const toggleNavigation = (event) => {
    event.preventDefault();
    const navigation = document.querySelector('.main-navigation');
    if (navigation) {
      navigation.classList.toggle('extended');
    }
  };

  /**
   * Add platform class to HTML element
   */
  const addPlatformClass = () => {
    const htmlElement = document.querySelector && document.querySelector('html');
    if (htmlElement) {
      const platformClass = getPlatformClassName();
      if (platformClass) {
        htmlElement.classList.add(platformClass);
      }
    }
  };

  /**
   * Initialize navigation toggle listener
   */
  const initNavigationToggle = () => {
    const toggleButton = document.querySelector('.js-extend-main-navigation');
    if (toggleButton) {
      toggleButton.addEventListener('click', toggleNavigation, false);
    }
  };

  /**
   * Initialize application
   */
  const init = () => {
    initNavigationToggle();
    addPlatformClass();
  };

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    // DOM is already ready
    init();
  }

})();
