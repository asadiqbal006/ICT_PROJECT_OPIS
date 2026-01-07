/**
 * OPIS - Simple JavaScript Animations
 */

// Wait for DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // ===== FADE IN ANIMATION FOR CARDS =====
  const cards = document.querySelectorAll(".card");
  cards.forEach((card, index) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(20px)";
    card.style.transition = "opacity 0.6s ease, transform 0.6s ease";

    setTimeout(() => {
      card.style.opacity = "1";
      card.style.transform = "translateY(0)";
    }, index * 100); // Stagger animation
  });

  // ===== SMOOTH PROGRESS BAR ANIMATION =====
  const progressBars = document.querySelectorAll(
    '[role="progressbar"][data-width]'
  );
  progressBars.forEach((bar, index) => {
    const targetWidth = parseFloat(bar.getAttribute("data-width"));
    bar.style.width = "0%";
    bar.style.transition = "width 1.5s ease-out";

    setTimeout(() => {
      bar.style.width = targetWidth + "%";
    }, 300 + index * 200); // Stagger progress bars
  });

  // ===== BUTTON HOVER EFFECTS =====
  const buttons = document.querySelectorAll(".btn, .ocean-btn");
  buttons.forEach((button) => {
    button.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-2px) scale(1.02)";
    });

    button.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0) scale(1)";
    });
  });

  // ===== FORM FIELD FOCUS ANIMATIONS =====
  const formFields = document.querySelectorAll(".form-select, .form-control");
  formFields.forEach((field) => {
    field.addEventListener("focus", function () {
      this.style.transform = "scale(1.02)";
      this.style.transition = "transform 0.2s ease";
    });

    field.addEventListener("blur", function () {
      this.style.transform = "scale(1)";
    });
  });

  // ===== BADGE PULSE ANIMATION =====
  const badges = document.querySelectorAll(".badge");
  badges.forEach((badge, index) => {
    badge.style.opacity = "0";
    badge.style.transform = "scale(0.8)";
    badge.style.transition = "opacity 0.4s ease, transform 0.4s ease";

    setTimeout(() => {
      badge.style.opacity = "1";
      badge.style.transform = "scale(1)";
    }, 500 + index * 100);
  });

  // ===== ALERT SLIDE IN ANIMATION =====
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach((alert, index) => {
    alert.style.opacity = "0";
    alert.style.transform = "translateX(-20px)";
    alert.style.transition = "opacity 0.5s ease, transform 0.5s ease";

    setTimeout(() => {
      alert.style.opacity = "1";
      alert.style.transform = "translateX(0)";
    }, 800 + index * 150);
  });

  // ===== ICON ROTATION ON HOVER =====
  const icons = document.querySelectorAll(".bi");
  icons.forEach((icon) => {
    icon.style.transition = "transform 0.3s ease";
    icon.addEventListener("mouseenter", function () {
      this.style.transform = "rotate(10deg) scale(1.1)";
    });
    icon.addEventListener("mouseleave", function () {
      this.style.transform = "rotate(0) scale(1)";
    });
  });

  // ===== FORM SUBMISSION LOADING STATE =====
  const form = document.getElementById("oceanForm");
  if (form) {
    form.addEventListener("submit", function (e) {
      const submitButton = this.querySelector('button[type="submit"]');
      if (submitButton) {
        submitButton.innerHTML =
          '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span>Analyzing...';
        submitButton.disabled = true;
        submitButton.style.opacity = "0.7";
      }
    });
  }

  // ===== SMOOTH SCROLL TO TOP ON PAGE LOAD =====
  window.scrollTo({ top: 0, behavior: "smooth" });

  // ===== ANIMATE NUMBERS IN BADGES (if present) =====
  const numberBadges = document.querySelectorAll(".badge.fs-6");
  numberBadges.forEach((badge) => {
    const text = badge.textContent;
    const number = parseFloat(text);
    if (!isNaN(number)) {
      badge.textContent = "0%";
      let current = 0;
      const increment = number / 30; // 30 steps
      const timer = setInterval(() => {
        current += increment;
        if (current >= number) {
          current = number;
          clearInterval(timer);
        }
        badge.textContent = Math.round(current) + "%";
      }, 30);
    }
  });
});
