$(document).ready(function () {

  // Check for click events on the navbar burger icon
  $(".navbar-burger").click(function () {

    // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
    $(".navbar-burger").toggleClass("is-active");
    $(".navbar-menu").toggleClass("is-active");

  });

  // jQuery UI datepicker, create task page
  $(function () {
    $("#datepicker").datepicker({
      dateFormat: 'yy mm dd',
      minDate: -60,
      maxDate: "+24M"
    });
    $("#format").on("change", function () {
      $("#datepicker").datepicker("option", "dateFormat", 'yy mm dd');
    });
  });

  // Replaces underscore spaces from MongoDB data with spaces
  const enemyName = document.querySelectorAll('.enemy-name')
  enemyName.forEach(e => e.innerText = e.innerText.replaceAll('_', ' '))
  const treasureName = document.querySelectorAll('.treasure-name')
  treasureName.forEach(e => e.innerText = e.innerText.replaceAll('_', ' '))
  const treasureInfo = document.querySelectorAll('.treasure-info')
  treasureInfo.forEach(e => e.innerText = e.innerText.replaceAll('_', ' '))

  document.addEventListener('DOMContentLoaded', () => {
    // Functions to open and close a modal
    function openModal($el) {
      $el.classList.add('is-active');
    }

    function closeModal($el) {
      $el.classList.remove('is-active');
    }

    function closeAllModals() {
      (document.querySelectorAll('.modal') || []).forEach(($modal) => {
        closeModal($modal);
      });
    }

    // Add a click event on buttons to open a specific modal
    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
      const modal = $trigger.dataset.target;
      const $target = document.getElementById(modal);
      console.log($target);

      $trigger.addEventListener('click', () => {
        openModal($target);
      });
    });

    // Add a click event on various child elements to close the parent modal
    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot .button') || []).forEach(($close) => {
      const $target = $close.closest('.modal');

      $close.addEventListener('click', () => {
        closeModal($target);
      });
    });

    // Add a keyboard event to close all modals
    document.addEventListener('keydown', (event) => {
      const e = event || window.event;

      if (e.keyCode === 27) { // Escape key
        closeAllModals();
      }
    });
  });

  document.addEventListener('DOMContentLoaded', () => {
    (document.querySelectorAll('.notification .delete') || []).forEach(($delete) => {
      const $notification = $delete.parentNode;

      $delete.addEventListener('click', () => {
        $notification.parentNode.removeChild($notification);
      });
    });
  });

});