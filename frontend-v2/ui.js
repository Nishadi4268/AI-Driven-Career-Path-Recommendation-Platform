export function renderChips(container, skills) {
  container.innerHTML = skills
    .map(
      (skill, i) =>
        `<span class="chip">${skill}<button class="remove" aria-label="Remove ${skill}" data-index="${i}">✕</button></span>`
    )
    .join("");
}

export function attachChipHandlers(container, onRemove) {
  container.addEventListener("click", (e) => {
    const btn = e.target.closest("button.remove");
    if (!btn) return;
    const idx = Number(btn.dataset.index);
    onRemove(idx);
  });
}

export function setLoading(btn, loading) {
  btn.disabled = loading;
  btn.textContent = loading ? "Fetching…" : "Get Recommendations";
}

export function showEmptyState(emptyEl, show) {
  emptyEl.hidden = !show;
}

export function showError(errorEl, message) {
  if (!message) {
    errorEl.hidden = true;
    errorEl.textContent = "";
    return;
  }
  errorEl.hidden = false;
  errorEl.textContent = message;
}

export function clearResults(output) {
  output.innerHTML = "";
}

export function addToast(toastsEl, message, type = "info", timeout = 3500) {
  const el = document.createElement("div");
  el.className = `toast ${type}`;
  el.textContent = message;
  toastsEl.appendChild(el);
  setTimeout(() => el.remove(), timeout);
}

export function buildResultCard(result, input) {
  const card = document.createElement("div");
  card.className = "card";

  // Calculate skill completion based on required vs missing skills
  const totalRequired = result.total_required || result.missing_skills?.length || 1;
  const missing = result.missing_skills?.length || 0;
  const completed = totalRequired - missing;
  const percent = Math.round((completed / totalRequired) * 100);

  const missingSkillsHtml = (result.missing_skills || [])
    .map((skill) => `<span class="skill-tag missing">${skill}</span>`)
    .join("");

  const roadmapHtml = (result.roadmap || [])
    .map((step, idx) => `<li class="roadmap-item"><span class="step-number">${idx + 1}</span>${step}</li>`)
    .join("");

  // Build course suggestions HTML
  const courseSuggestionsHtml = (result.course_suggestions || []).map(item => {
    const coursesHtml = item.courses.map(course => `
      <div class="course-card">
        <div class="course-header">
          <strong>${course.title}</strong>
          <span class="course-level">${course.level}</span>
        </div>
        <div class="course-meta">
          <span class="platform-badge">${course.platform}</span>
          <span class="duration">⏱️ ${course.duration}</span>
        </div>
        <a href="${course.url}" target="_blank" rel="noopener noreferrer" class="course-link">View Course →</a>
      </div>
    `).join("");
    
    return `
      <div class="skill-courses">
        <h4>📚 ${item.skill}</h4>
        ${coursesHtml}
      </div>
    `;
  }).join("");

  // Status message based on completion
  let statusMessage = '';
  let statusClass = '';
  if (percent === 100) {
    statusMessage = '🎉 Perfect match! You have all required skills.';
    statusClass = 'status-excellent';
  } else if (percent >= 75) {
    statusMessage = '🌟 Great fit! Just a few skills to learn.';
    statusClass = 'status-good';
  } else if (percent >= 50) {
    statusMessage = '💪 Good foundation! Some learning ahead.';
    statusClass = 'status-moderate';
  } else {
    statusMessage = '🚀 Exciting journey ahead! Let\'s get started.';
    statusClass = 'status-beginner';
  }

  card.innerHTML = `
    <div class="career-hero">
      <div class="career-icon">💼</div>
      <div class="career-info">
        <h2 class="career-title">${result.recommended_career}</h2>
        <div class="career-subtitle">Based on: ${input.skills}</div>
      </div>
    </div>

    <div class="status-banner ${statusClass}">
      ${statusMessage}
    </div>

    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-value">${completed}/${totalRequired}</div>
        <div class="stat-label">Skills Match</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${percent}%</div>
        <div class="stat-label">Completion</div>
      </div>
      <div class="stat-card">
        <div class="stat-value">${missing}</div>
        <div class="stat-label">To Learn</div>
      </div>
    </div>

    <div class="progress-section">
      <div class="progress-header">
        <span class="progress-label">Your Progress</span>
        <span class="progress-percent">${percent}%</span>
      </div>
      <div class="progress-bar">
        <div class="progress" style="width:${percent}%"></div>
      </div>
    </div>

    ${missing > 0 ? `
    <div class="info-section">
      <h3 class="section-title">🎯 Skills to Develop</h3>
      <div class="skills-grid">${missingSkillsHtml}</div>
    </div>
    ` : `
    <div class="info-section success">
      <h3 class="section-title">✅ All Skills Satisfied!</h3>
      <p class="success-message">You have all the required skills for this career path.</p>
    </div>
    `}

    ${roadmapHtml ? `
    <div class="info-section">
      <h3 class="section-title">🗺️ Learning Roadmap</h3>
      <ul class="roadmap-list">${roadmapHtml}</ul>
    </div>
    ` : ''}

    ${courseSuggestionsHtml ? `
    <div class="courses-section">
      <h3 class="section-title">📖 Recommended Courses</h3>
      <p class="section-desc">Start with these curated courses from top platforms</p>
      ${courseSuggestionsHtml}
    </div>
    ` : ''}
  `;
  return card;
}
