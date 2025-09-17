const ROWS = 6;
const COLS = 7;
let board = Array.from({ length: ROWS }, () => Array(COLS).fill(null));
let currentPlayer = 'red';

const gameBoard = document.getElementById('gameBoard');
const statusText = document.getElementById('status');

// Crear celdas
for (let r = 0; r < ROWS; r++) {
  for (let c = 0; c < COLS; c++) {
    const cell = document.createElement('div');
    cell.classList.add('cell');
    cell.dataset.row = r;
    cell.dataset.col = c;
    cell.addEventListener('click', handleClick);
    gameBoard.appendChild(cell);
  }
}

function handleClick(e) {
  const col = parseInt(e.target.dataset.col);
  for (let row = ROWS - 1; row >= 0; row--) {
    if (!board[row][col]) {
      board[row][col] = currentPlayer;
      const cell = document.querySelector(
        `.cell[data-row="${row}"][data-col="${col}"]`
      );
      cell.classList.add(currentPlayer);
      if (checkWin(row, col)) {
        statusText.textContent = `¡${currentPlayer === 'red' ? '🔴' : '🟡'} gana!`;
        gameBoard.style.pointerEvents = 'none';
      } else {
        currentPlayer = currentPlayer === 'red' ? 'yellow' : 'red';
        statusText.textContent = `Turno del jugador: ${currentPlayer === 'red' ? '🔴' : '🟡'}`;
      }
      break;
    }
  }
}

function checkWin(row, col) {
  const directions = [
    [[0, 1], [0, -1]],     // Horizontal
    [[1, 0], [-1, 0]],     // Vertical
    [[1, 1], [-1, -1]],    // Diagonal \
    [[1, -1], [-1, 1]]     // Diagonal /
  ];

  for (let dir of directions) {
    let count = 1;
    for (let [dr, dc] of dir) {
      let r = row + dr;
      let c = col + dc;
      while (
        r >= 0 && r < ROWS &&
        c >= 0 && c < COLS &&
        board[r][c] === currentPlayer
      ) {
        count++;
        r += dr;
        c += dc;
      }
    }
    if (count >= 4) return true;
  }
  return false;
}