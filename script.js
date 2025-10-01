// --- Element Selection ---
const statusText = document.getElementById("status");
const boardDiv = document.getElementById("board");
const pvpBtn = document.getElementById("pvpBtn");
const pvcBtn = document.getElementById("pvcBtn");
const newGameBtn = document.getElementById("newGameBtn");
const popup = document.getElementById("popup");
const popupText = document.getElementById("popupText");
const popupOkBtn = document.getElementById("popupOkBtn");

// --- Audio Selection ---
const cellClick = document.getElementById("cellClick");
const btnClick = document.getElementById("btnClick");
const drawSound = document.getElementById("drawSound");
const winSound = document.getElementById("winSound");

// --- Game State Variables ---
let board = Array(9).fill("");
let currentPlayer = "X";
let gameMode = null;
let gameOver = false;

// --- Event Listeners ---
pvpBtn.addEventListener('click', () => setMode('pvp'));
pvcBtn.addEventListener('click', () => setMode('pvc'));
newGameBtn.addEventListener('click', resetGame);
popupOkBtn.addEventListener('click', closePopup);

// Unlock audio on first user interaction
document.addEventListener("click", function unlockAudio() {
    [cellClick, btnClick, drawSound, winSound].forEach(sound => {
        sound.play().then(() => sound.pause()).catch(() => {});
    });
    document.removeEventListener("click", unlockAudio);
});

// --- Game Functions ---
function createBoard() {
    boardDiv.innerHTML = ''; // Clear board for resets
    for (let i = 0; i < 9; i++) {
        const cell = document.createElement("div");
        cell.className = "cell";
        cell.dataset.index = i;
        cell.addEventListener('click', () => makeMove(i));
        boardDiv.appendChild(cell);
    }
}

function buttonClickSound() {
    btnClick.currentTime = 0;
    btnClick.play().catch(() => {});
}

function setMode(mode) {
    buttonClickSound();
    gameMode = mode;
    resetGame();
}

function resetGame() {
    buttonClickSound();
    board.fill("");
    gameOver = false;
    currentPlayer = "X";
    document.querySelectorAll(".cell").forEach(cell => {
        cell.textContent = "";
        cell.className = "cell";
    });
    statusText.textContent = gameMode ? `${currentPlayer}'s turn` : "Select Game Mode";
    closePopup();
}

function makeMove(index) {
    if (board[index] !== "" || gameOver || !gameMode) {
        return;
    }

    board[index] = currentPlayer;
    const cell = document.querySelector(`.cell[data-index="${index}"]`);
    cell.textContent = currentPlayer;
    cell.classList.add("taken");

    cellClick.currentTime = 0;
    cellClick.play().catch(() => {});

    if (checkWinner(currentPlayer)) {
        statusText.textContent = `${currentPlayer} wins!`;
        highlightWinningCells(currentPlayer);
        winSound.playbackRate = 1.5;
        winSound.currentTime = 0;
        winSound.play().catch(() => {});
        showPopup(`${currentPlayer} WINS!`);
        gameOver = true;
    } else if (!board.includes("")) {
        statusText.textContent = "It's a draw!";
        drawSound.currentTime = 0;
        drawSound.play().catch(() => {});
        showPopup("It's a Draw!");
        gameOver = true;
    } else {
        currentPlayer = currentPlayer === "X" ? "O" : "X";
        statusText.textContent = `${currentPlayer}'s turn`;
    }
}

function checkWinner(player) {
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]             // Diagonals
    ];
    return winningCombinations.some(combination => {
        return combination.every(index => board[index] === player);
    });
}

function highlightWinningCells(player) {
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ];
    winningCombinations.forEach(combination => {
        if (combination.every(index => board[index] === player)) {
            combination.forEach(index => {
                document.querySelector(`[data-index="${index}"]`).classList.add("winner");
            });
        }
    });
}

function showPopup(message) {
    popupText.textContent = `🎉 ${message} 🎉`;
    popup.style.display = "flex";
}

function closePopup() {
    popup.style.display = "none";
}

// Initialize the game board on page load
createBoard();