const qs = (selector, root = document) => root.querySelector(selector);

function createElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined) element.textContent = text;
  return element;
}

function renderList(target, items) {
  target.innerHTML = "";
  items.forEach((item) => {
    const li = createElement("li", "", item);
    target.appendChild(li);
  });
}

function renderHero(data) {
  qs("#heroSubtitle").textContent = data.hero.subtitle;
  qs("#heroOneLiner").textContent = data.hero.oneLiner;
  qs("#heroNote").textContent = data.hero.note;
  qs("#primaryCta").textContent = data.hero.primaryCta.label;
  qs("#primaryCta").href = data.hero.primaryCta.href;
  qs("#secondaryCta").textContent = data.hero.secondaryCta.label;
  qs("#secondaryCta").href = data.hero.secondaryCta.href;

  const stats = qs("#heroStats");
  stats.innerHTML = "";
  data.hero.stats.forEach((stat) => {
    const card = createElement("article", "stat-card");
    card.appendChild(createElement("span", "", stat.label));
    card.appendChild(createElement("strong", "", stat.value));
    card.appendChild(createElement("small", "", stat.detail));
    stats.appendChild(card);
  });
}

function renderPrompt(data) {
  qs("#promptText").textContent = data.prompt.text;
  renderList(qs("#promptNotes"), data.prompt.notes);

  qs("#promptBox").addEventListener("click", async () => {
    const hint = qs(".copy-hint");
    try {
      await navigator.clipboard.writeText(data.prompt.text);
      hint.textContent = "已复制";
    } catch {
      hint.textContent = "复制失败，请手动选择";
    }
    window.setTimeout(() => {
      hint.textContent = "点击复制 prompt";
    }, 1600);
  });
}

function renderWorkflow(data) {
  const container = qs("#workflowSteps");
  container.innerHTML = "";

  data.workflow.forEach((step, index) => {
    const card = createElement("article", "workflow-card");
    card.appendChild(createElement("span", "step-index", String(index + 1)));
    card.appendChild(createElement("h3", "", step.name));
    card.appendChild(createElement("p", "muted", step.description));
    container.appendChild(card);
  });
}

function renderRepoToResume(data) {
  const repo = data.repoToResume.inputProject;
  qs("#repoName").textContent = repo.name;
  qs("#repoOneSentence").textContent = repo.oneSentence;

  const repoLinks = qs("#repoLinks");
  repoLinks.innerHTML = "";
  [
    ["GitHub", repo.githubUrl],
    ["GitHub Pages", repo.githubPagesUrl],
    ["Vercel Demo", repo.vercelUrl],
  ].forEach(([label, href]) => {
    const link = createElement("a", "repo-link", label);
    link.href = href;
    link.target = "_blank";
    link.rel = "noreferrer";
    repoLinks.appendChild(link);
  });

  const chips = qs("#sourceChips");
  chips.innerHTML = "";
  repo.sources.forEach((source) => {
    chips.appendChild(createElement("span", "source-chip", source));
  });

  qs("#skillPositioning").textContent = data.repoToResume.positioning.skillOutput;
  qs("#resumePositioning").textContent = data.repoToResume.positioning.resumeReady;
  renderList(qs("#repoExpression"), data.repoToResume.translation.repoExpression);
  renderList(qs("#pmExpression"), data.repoToResume.translation.pmExpression);

  const resumeOutputs = qs("#resumeOutputs");
  resumeOutputs.innerHTML = "";
  data.repoToResume.resumeOutputs.forEach((item, index) => {
    const card = createElement("article", "resume-bullet");
    card.appendChild(createElement("span", "bullet-index", `0${index + 1}`));
    card.appendChild(createElement("p", "claim-label", item.label));
    card.appendChild(createElement("p", "", item.text));
    resumeOutputs.appendChild(card);
  });

  const blocked = qs("#blockedResumeClaims");
  blocked.innerHTML = "";
  data.repoToResume.blockedResumeClaims.forEach((claim) => {
    blocked.appendChild(createElement("span", "", claim));
  });

  const outline = qs("#portfolioOutline");
  outline.innerHTML = "";
  data.repoToResume.portfolioOutline.forEach((item, index) => {
    const row = createElement("article", "outline-row");
    row.appendChild(createElement("span", "outline-index", String(index + 1)));
    const copy = createElement("div");
    copy.appendChild(createElement("h4", "", item.title));
    copy.appendChild(createElement("p", "muted", item.description));
    row.appendChild(copy);
    outline.appendChild(row);
  });

  qs("#interviewPitch").textContent = data.repoToResume.interviewPitch;
  renderList(qs("#safeClaims"), data.repoToResume.boundary.safeClaims);
  renderList(qs("#blockedClaims"), data.repoToResume.boundary.blockedClaims);
}

function renderOutputs(data) {
  qs("#outputsIntro").textContent = data.outputs.intro;
  const cards = qs("#outputCards");
  cards.innerHTML = "";

  data.outputs.files.forEach((item) => {
    const card = createElement("article", "output-card");
    card.tabIndex = 0;
    card.setAttribute("role", "button");
    card.setAttribute("aria-expanded", "false");

    const head = createElement("div", "output-head");
    head.appendChild(createElement("span", "file-name", item.file));
    head.appendChild(createElement("span", `status ${item.status}`, item.status));
    card.appendChild(head);

    card.appendChild(createElement("p", "purpose", item.purpose));
    card.appendChild(createElement("span", "audience", item.audience));

    const detail = createElement("div", "card-detail");
    detail.appendChild(createElement("p", "", item.detail));
    card.appendChild(detail);

    const toggle = () => {
      const open = card.classList.toggle("open");
      card.setAttribute("aria-expanded", String(open));
    };

    card.addEventListener("click", toggle);
    card.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        toggle();
      }
    });

    cards.appendChild(card);
  });
}

function renderEvaluation(data) {
  const evaluation = data.evaluation;
  qs("#scoreValue").textContent = `${evaluation.total} / ${evaluation.max} · ${evaluation.level}`;
  qs("#scoreDefinition").textContent = evaluation.definition;

  const bars = qs("#scoreBars");
  bars.innerHTML = "";
  evaluation.dimensions.forEach((dimension) => {
    const row = createElement("article", dimension.risk ? "score-row risk" : "score-row");
    const head = createElement("div", "score-head");
    head.appendChild(createElement("span", "", dimension.name));
    head.appendChild(createElement("strong", "", `${dimension.score} / 2`));

    const bar = createElement("div", "bar");
    const fill = createElement("div", "bar-fill");
    fill.style.setProperty("--target-width", `${(dimension.score / 2) * 100}%`);
    bar.appendChild(fill);

    row.appendChild(head);
    row.appendChild(bar);
    row.appendChild(createElement("p", "muted", dimension.note));
    bars.appendChild(row);
  });

  renderList(qs("#strengths"), evaluation.strengths);
  renderList(qs("#weaknesses"), evaluation.weaknesses);
}

function renderComparison(data) {
  renderList(qs("#beforeList"), data.beforeAfter.before);
  renderList(qs("#afterList"), data.beforeAfter.after);
}

function renderIteration(data) {
  const timeline = qs("#iterationTimeline");
  timeline.innerHTML = "";

  data.iteration.forEach((entry) => {
    const item = createElement("article", "timeline-item");
    item.appendChild(createElement("span", "version-pill", entry.version));
    item.appendChild(createElement("h3", "", entry.title));

    const detail = createElement("div", "timeline-detail");
    detail.appendChild(createElement("p", "", `问题：${entry.problem}`));
    detail.appendChild(createElement("p", "", `优化：${entry.optimization}`));
    detail.appendChild(createElement("p", "", `结果：${entry.result}`));
    item.appendChild(detail);
    timeline.appendChild(item);
  });
}

function renderRoadmap(data) {
  const grid = qs("#roadmapGrid");
  grid.innerHTML = "";

  Object.entries(data.roadmap).forEach(([stage, items]) => {
    const card = createElement("article", stage === "P0" ? "roadmap-card focus" : "roadmap-card");
    card.appendChild(createElement("h3", "", stage));
    const list = createElement("ul");
    renderList(list, items);
    card.appendChild(list);
    grid.appendChild(card);
  });
}

function renderBoundaries(data) {
  renderList(qs("#evidenceBoundaries"), data.evidenceBoundaries);
}

function animateScoreBars() {
  const bars = Array.from(document.querySelectorAll(".bar-fill"));
  if (!("IntersectionObserver" in window)) {
    bars.forEach((bar) => bar.classList.add("active"));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("active");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.35 }
  );

  bars.forEach((bar) => observer.observe(bar));
}

function renderPage(data) {
  renderHero(data);
  renderPrompt(data);
  renderWorkflow(data);
  renderRepoToResume(data);
  renderOutputs(data);
  renderEvaluation(data);
  renderComparison(data);
  renderIteration(data);
  renderRoadmap(data);
  renderBoundaries(data);
  animateScoreBars();
}

async function loadData() {
  const response = await fetch("data/showcase-data.json", { cache: "no-store" });
  if (!response.ok) {
    throw new Error(`Failed to load showcase data: ${response.status}`);
  }
  return response.json();
}

document.addEventListener("DOMContentLoaded", async () => {
  try {
    const data = await loadData();
    renderPage(data);
  } catch (error) {
    const main = qs("main");
    const message = createElement("section", "section load-error");
    message.innerHTML = `
      <div class="section-heading">
        <p class="eyebrow">Load Error</p>
        <h2>无法加载展示数据</h2>
        <p class="muted">请通过本地静态服务器或 GitHub Pages 打开此页面，例如在项目根目录运行 <code>python -m http.server 8000</code> 后访问 <code>http://localhost:8000/docs/skill-showcase/</code>。</p>
      </div>
    `;
    main.prepend(message);
    console.error(error);
  }
});
