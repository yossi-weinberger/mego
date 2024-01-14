//----------------------------------------------------
///puts the canvas in the html to show
canvas = document.getElementById("myCanvas");
ctx = canvas.getContext("2d");



// constant movment by direction

function game_play() {

  //plays aoudio
window.onload = function () {
  song.play();
};

document.body.onkeydown = function () {
  song.play();
};

  document.getElementById("score").innerHTML = score;
  document.getElementById("lives").innerHTML = lives;

  //cleans canvas
  ctx.drawImage(moon_img, 0, 0, 500, 500);

  // draws apple player enemys and walls
  apple();
  player();
  enemys();
  drow_walls();
}

//----------------------------------------------------
function key_strike() {
  // putting new valeus of player diraction
  if (event.keyCode == 40 && y < 480 && y >= 0) direction = "d";
  if (event.keyCode == 38 && y <= 480 && y > 0) direction = "u";
  if (event.keyCode == 37 && x <= 480 && x > 0) direction = "l";
  if (event.keyCode == 39 && x < 480 && x >= 0) direction = "r";
}

function apple() {
  ctx.drawImage(apple_img, apple_x, apple_y, block_size, block_size);
}

function player() {
  // putting new valeus of player location
  if (direction == "d" && y < 500 && y >= 0) y += block_size;
  if (direction == "u" && y <= 500 && y > -block_size) y -= block_size;
  if (direction == "l" && x <= 500 && x > -block_size) x -= block_size;
  if (direction == "r" && x < 500 && x >= 0) x += block_size;

  //player poping from the other side
  if (direction == "d" && y >= 500) y = 0;
  if (direction == "u" && y <= -20) y = 480;
  if (direction == "r" && x >= 500) x = 0;
  if (direction == "l" && x <= -20) x = 480;

  //if player meets enemys
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    if (x == enemy.enemy_x && y == enemy.enemy_y) {
      hit_sound.play();
      window.alert("You lost 1 live!");
      lives -= 1;
    }
    if (direction == "l" && x + 20 == enemy.enemy_x && y == enemy.enemy_y) {
      hit_sound.play();
      window.alert("You lost 1 live!");
      lives -= 1;
    }
  }
//resat if game over
  if (lives == 0) {
    window.alert("game over!!!\n");
    score = 0;
    lives = 3;
  }

  //if player meets apple
  if (x == apple_x && y == apple_y) {
    //place the apple in a new random location
    bite_sound.play();
    xr = Math.floor(Math.random() * 460);
    yr = Math.floor(Math.random() * 460);
    apple_x = xr + (20 - (xr % 20));
    apple_y = yr + (20 - (yr % 20));
    score += 1;
  }

  //if player meets wall
  for (let step = 0; step < walls.length; step++) {
    if (
      direction == "u" &&
      x == walls[step].x &&
      y == walls[step].y + block_size
    ) {
      direction = "stop";
    } else if (
      direction == "d" &&
      x == walls[step].x &&
      y == walls[step].y - block_size
    ) {
      direction = "stop";
    } else if (
      direction == "l" &&
      x == walls[step].x + block_size &&
      y == walls[step].y
    ) {
      direction = "stop";
    } else if (
      direction == "r" &&
      x == walls[step].x - block_size &&
      y == walls[step].y
    ) {
      direction = "stop";
    }

    //set the privios direction
    previos_direction = direction;

    //draw player in curent direction
    if (direction == "r") ctx.drawImage(player_r, x, y, block_size, block_size);
    else if (direction == "l")
      ctx.drawImage(player_l, x, y, block_size, block_size);
    else if (direction == "u")
      ctx.drawImage(player_b, x, y, block_size, block_size);
    else if (direction == "d")
      ctx.drawImage(player_f, x, y, block_size, block_size);
    else if (direction == "stop")
      ctx.drawImage(player_s, x, y, block_size, block_size);
  }
}

function enemys() {
  // draw enemys
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    ctx.drawImage(enemy_img, enemy.enemy_x,enemy.enemy_y,block_size,block_size);
  }

  //enemies poping from the other side
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    if (enemy.enemy_y >= 500) enemy.enemy_y = 0;
    if (enemy.enemy_x >= 500) enemy.enemy_x = 0;
  }

  // movment of enemys
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    if (
      (direction == "d" && enemy.enemy_y != y) ||
      (direction == "u" && enemy.enemy_y != y)
    )
      enemy.enemy_y += block_size;
    if (
      (direction == "d" && enemy.enemy_y == y) ||
      (direction == "u" && enemy.enemy_y == y)
    )
      enemy.enemy_x += block_size;
    if (
      (direction == "l" && enemy.enemy_y != y) ||
      (direction == "r" && enemy.enemy_y != y)
    )
      enemy.enemy_y += block_size;
    if (
      (direction == "l" && enemy.enemy_y == y) ||
      (direction == "r" && enemy.enemy_y == y)
    )
      enemy.enemy_x += block_size;
    if (direction == "stop") enemy.enemy_x += block_size;
  }
}

function drow_walls() {
  for (var i = 0; i < walls.length; i++)
    ctx.drawImage(brick_img, walls[i].x, walls[i].y, block_size, block_size);

  for (var i = 0; i < portals.length; i++)
    ctx.drawImage(portal_img,portals[i].x,portals[i].y,block_size,block_size);
}

//creating screen by array
var screen = Array(
  1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  2,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,2,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,
  1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1);


walls = new Array();
portals = new Array();

//drows screen with matrix
screen_x = 0;
screen_y = 0;

for (var i = 0; i < screen.length; i++) {
  screen_x = i % 25;
  screen_y = Math.floor(i / 25);

  if (screen[i] == 1) {
    walls.push({ x: screen_x * 20, y: screen_y * 20 });
  } else if (screen[i] == 2) {
    portals.push({ x: screen_x * 20, y: screen_y * 20 });
  }
}

//vars and pics

//player starting point
var x = 40;
var y = 40;

//player pics - 5 angels
var player_r = new Image();
player_r.src = "pics/rick_right.png";

var player_l = new Image();
player_l.src = "pics/rick_left.png";

var player_f = new Image();
player_f.src = "pics/rick_front.png";

var player_b = new Image();
player_b.src = "pics/rick_back.png";

var player_s = new Image();
player_s.src = "pics/rick_stop.png";

//elements pics
var moon_img = new Image();
moon_img.src = "moon.jpg";

var brick_img = new Image();
brick_img.src = "brick.png";

var enemy_img = new Image();
enemy_img.src = "pics/enemy3.svg";

var apple_img = new Image();
apple_img.src = "pics/seed.webp";

var portal_img = new Image();
portal_img.src = "portal.png";

//sounds
let song = new Audio();
song.src = "sound/background.ogg";
song.loop = true;

var hit_sound = new Audio();
hit_sound.src = "sound/hit.wav";

var bite_sound = new Audio();
bite_sound.src = "sound/bite.wav";

// creating random num for apple and enemies
function random_num() {
  return Math.floor(Math.random() * 24) * 20 + 20;
}

//putts apple in random location
var apple_x = random_num() + (20 - (random_num() % 20));
var apple_y = random_num() + (20 - (random_num() % 20));

// enemys
enemies = new Array();

enemy_3 = {
  enemy_x: random_num() + (20 - (random_num() % 20)),
  enemy_y: random_num() + (20 - (random_num() % 20)),
};

enemy_4 = {
  enemy_x: random_num() + (20 - (random_num() % 20)),
  enemy_y: random_num() + (20 - (random_num() % 20)),
};

enemies.push(enemy_3, enemy_4);

var previos_direction = 0;
var score = 0;
var lives = 3;
var block_size = 20;
var direction = "r";

//calls script
document.onkeydown = key_strike;
// constent movment
time = 180;
setInterval(game_play, time);
