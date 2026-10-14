// ShareForge web app. Built by Mourad.Soltani

const titleEl = document.getElementById("title");
const descEl = document.getElementById("description");
const imageEl = document.getElementById("image");
const siteEl = document.getElementById("site");
const urlEl = document.getElementById("url");
const outputEl = document.getElementById("output");
const titleCount = document.getElementById("title-count");
const descCount = document.getElementById("desc-count");

function escapeHtml(str) {
  return str
    .replace(/&/g, "&")
    .replace(/"/g, """)
    .replace(/</g, "<")
    .replace(/>/g, ">");
}

function generateTags() {
  const title = titleEl.value.trim() || "Untitled";
  const description = descEl.value.trim() || "No description provided.";
  const image = imageEl.value.trim();
  const site = siteEl.value.trim();
  const url = urlEl.value.trim();

  let tags = `<meta name="description" content="${escapeHtml(description)}">\n`;
  tags += `<meta property="og:title" content="${escapeHtml(title)}">\n`;
  tags += `<meta property="og:description" content="${escapeHtml(description)}">\n`;
  tags += `<meta property="og:type" content="website">\n`;
  if (url) tags += `<meta property="og:url" content="${escapeHtml(url)}">\n`;
  if (image) tags += `<meta property="og:image" content="${escapeHtml(image)}">\n`;
  if (site) tags += `<meta property="og:site_name" content="${escapeHtml(site)}">\n`;
  tags += `<meta name="twitter:card" content="summary_large_image">\n`;
  tags += `<meta name="twitter:title" content="${escapeHtml(title)}">\n`;
  tags += `<meta name="twitter:description" content="${escapeHtml(description)}">\n`;
  if (image) tags += `<meta name="twitter:image" content="${escapeHtml(image)}">\n`;

  outputEl.textContent = tags.trim();

  // Update previews
  document.querySelectorAll(".card-title").forEach(el => el.textContent = title);
  document.querySelectorAll(".card-desc").forEach(el => el.textContent = description);
  document.querySelectorAll(".card-domain").forEach(el => {
    try {
      el.textContent = url ? new URL(url).hostname : "yoursite.com";
    } catch { el.textContent = "yoursite.com"; }
  });
  document.querySelectorAll(".card-image").forEach(el => {
    el.style.backgroundImage = image ? `url(${image})` : "none";
    el.style.backgroundColor = image ? "transparent" : "#cbd5e1";
  });
}

function updateCounts() {
  titleCount.textContent = titleEl.value.length;
  descCount.textContent = descEl.value.length;
}

["input", "change"].forEach(ev => {
  titleEl.addEventListener(ev, () => { updateCounts(); generateTags(); });
  descEl.addEventListener(ev, () => { updateCounts(); generateTags(); });
  imageEl.addEventListener(ev, generateTags);
  siteEl.addEventListener(ev, generateTags);
  urlEl.addEventListener(ev, generateTags);
});

document.getElementById("generate").addEventListener("click", generateTags);
document.getElementById("copy").addEventListener("click", () => {
  navigator.clipboard.writeText(outputEl.textContent).then(() => alert("Copied!"));
});

// Initial
updateCounts();
generateTags();
