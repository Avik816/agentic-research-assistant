const downloadArea = document.getElementById("downloadArea");
const downloadList = document.getElementById("downloadList");


/* Add downloadable paper/file */
export function addDownloadItem(filename, url) {

    // Show download section when first file arrives
    downloadArea.classList.remove("hidden");

    const paperDiv = document.createElement("div");

    paperDiv.classList.add("paper-description");

    paperDiv.innerHTML = `
        <span class="paper-id">
            ${filename}
        </span>

        <a
            href="${url}"
            class="download-button"
            download
        >
            <img
                src="/static/assets/icons/download_button.svg"
                alt="download button"
            >
        </a>
    `;

    downloadList.appendChild(paperDiv);
}


/* Optional: clear downloads */
export function clearDownloads() {
    downloadList.innerHTML = "";
    downloadArea.classList.add("hidden");
}