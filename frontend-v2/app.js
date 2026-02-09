import { recommend, sendFeedback } from "./api.js";
import { renderChips, attachChipHandlers, setLoading, showEmptyState, showError, clearResults, addToast, buildResultCard, attachFeedbackHandlers } from "./ui.js";

const selectors = {
  chips: document.getElementById("skills-chips"),
  skillsInput: document.getElementById("skills-input"),
  interest: document.getElementById("interest"),
  education: document.getElementById("education"),
  educationOther: document.getElementById("education-other"),
  submitBtn: document.getElementById("submit-btn"),
  resetBtn: document.getElementById("reset-btn"),
  errorEl: document.getElementById("error"),
  output: document.getElementById("output"),
  empty: document.getElementById("empty-state"),
  toasts: document.getElementById("toasts"),
};

const state = {
  skills: JSON.parse(localStorage.getItem("skills") || "[]"),
};

function persist() {
  localStorage.setItem("skills", JSON.stringify(state.skills));
}

function render() {
  renderChips(selectors.chips, state.skills);
}

function addSkillChipFromInput() {
  const raw = selectors.skillsInput.value.trim();
  if (!raw) return;
  raw
    .split(",")
    .map((s) => s.trim())
    .filter(Boolean)
    .forEach((s) => state.skills.push(s));
  selectors.skillsInput.value = "";
  persist();
  render();
}

selectors.skillsInput.addEventListener("keydown", (e) => {
  if (e.key === "Enter") {
    e.preventDefault();
    addSkillChipFromInput();
  }
});

attachChipHandlers(selectors.chips, (idx) => {
  state.skills.splice(idx, 1);
  persist();
  render();
});

// Handle education dropdown - show custom input if "Other" selected
selectors.education.addEventListener("change", (e) => {
  if (e.target.value === "Other") {
    selectors.educationOther.style.display = "block";
    selectors.educationOther.focus();
  } else {
    selectors.educationOther.style.display = "none";
    selectors.educationOther.value = "";
  }
});

selectors.resetBtn.addEventListener("click", () => {
  state.skills = [];
  selectors.interest.value = "";
  selectors.education.value = "";
  selectors.educationOther.value = "";
  selectors.educationOther.style.display = "none";
  showError(selectors.errorEl, "");
  clearResults(selectors.output);
  showEmptyState(selectors.empty, true);
  persist();
  render();
  addToast(selectors.toasts, "Form cleared.");
});

selectors.submitBtn.addEventListener("click", submitForm);

async function submitForm() {
  // Auto-add any skills typed in the input field
  if (selectors.skillsInput.value.trim()) {
    addSkillChipFromInput();
  }

  const skills = state.skills.join(", ");
  const interest = selectors.interest.value.trim();
  const educationValue = selectors.education.value;
  const education = educationValue === "Other" 
    ? selectors.educationOther.value.trim() 
    : educationValue;

  showError(selectors.errorEl, "");
  clearResults(selectors.output);
  showEmptyState(selectors.empty, false);

  if (!skills || !interest || !education) {
    showError(selectors.errorEl, "Please add skills and fill all fields.");
    addToast(selectors.toasts, "Fill all fields to continue.", "error");
    return;
  }

  const payload = { skills, interest, education };
  setLoading(selectors.submitBtn, true);

  try {
    const result = await recommend(payload);
    const card = buildResultCard(result, payload);
    selectors.output.appendChild(card);
    attachFeedbackHandlers(card, result, payload, async (feedbackPayload) => {
      await sendFeedback(feedbackPayload);
      addToast(selectors.toasts, "Feedback sent. Thanks!");
    });
    addToast(selectors.toasts, "Recommendations ready.");
  } catch (err) {
    console.error(err);
    showError(selectors.errorEl, "Cannot reach the API. Is the backend running?");
    showEmptyState(selectors.empty, true);
    addToast(selectors.toasts, "Backend error: check server.", "error");
  } finally {
    setLoading(selectors.submitBtn, false);
  }
}

// Initialize
document.addEventListener("DOMContentLoaded", () => {
  render();
  showEmptyState(selectors.empty, true);
});
