// constant movment to direction
function game_play() {
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

  // movment of enemys
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
  if (
    (direction == "d" && enemy.enemy_y != y) || (direction == "u" && enemy.enemy_y != y))
    enemy.enemy_y += block_size;
  if (
    (direction == "d" && enemy.enemy_y == y) || (direction == "u" && enemy.enemy_y == y))
    enemy.enemy_x += block_size;
  if (
    (direction == "l" && enemy.enemy_y != y) || (direction == "r" && enemy.enemy_y != y))
    enemy.enemy_y += block_size;
  if (
    (direction == "l" && enemy.enemy_y == y) || (direction == "r" && enemy.enemy_y == y))
    enemy.enemy_x += block_size;
  if (direction == "stop" ) enemy.enemy_x += block_size;
  }

  // if (
  //   (direction == "d" && enemy_1y != y) || (direction == "u" && enemy_1y != y))
  //   enemy_1y += block_size;
  // if (
  //   (direction == "d" && enemy_1y == y) || (direction == "u" && enemy_1y == y))
  //   enemy_1x += block_size;
  // if (
  //   (direction == "l" && enemy_1y != y) || (direction == "r" && enemy_1y != y))
  //   enemy_1y += block_size;
  // if (
  //   (direction == "l" && enemy_1y == y) || (direction == "r" && enemy_1y == y))
  //   enemy_1x += block_size;
  // if (direction == "stop" ) enemy_1x += block_size;
  // // if (direction == "stop" && enemy_1x == x) enemy_1y += block_size;

  // if (
  //   (direction == "d" && enemy_2y != y) ||
  //   (direction == "u" && enemy_2y != y)
  // )
  //   enemy_2y += block_size;
  // if (
  //   (direction == "d" && enemy_2y == y) ||
  //   (direction == "u" && enemy_2y == y)
  // )
  //   enemy_2x += block_size;
  // if (
  //   (direction == "l" && enemy_2y != y) ||
  //   (direction == "r" && enemy_2y != y)
  // )
  //   enemy_2y += block_size;
  // if (
  //   (direction == "l" && enemy_2y == y) ||
  //   (direction == "r" && enemy_2y == y)
  // )
  // if (direction == "stop" ) 
  //   enemy_1x += block_size;
  //   enemy_2x += block_size;


  //enemies poping from the other side
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    if (enemy.enemy_y >= 500) enemy.enemy_y = 0;
    if (enemy.enemy_x >= 500) enemy.enemy_x = 0;
  }
  // if (enemy_1y >= 500) enemy_1y = 0;
  // if (enemy_1x >= 500) enemy_1x = 0;

  // if (enemy_2y >= 500) enemy_2y = 0;
  // if (enemy_2x >= 500) enemy_2x = 0;

  //if player meets enemys

  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    if (x == enemy.enemy_x && y == enemy.enemy_y) window.alert("Game-Over");
  }

  // if (x == enemy_1x && y == enemy_1y) {
  //   window.alert("Game-Over");
  // }
  // if (x == enemy_2x && y == enemy_2y) {
  //   window.alert("Game-Over");
  // }


  //if player meets apple
  if (x == apple_x && y == apple_y) {
    score += 1;

    //place the apple in a new random location
    xr = Math.floor(Math.random() * 480);
    yr = Math.floor(Math.random() * 480);
    apple_x = xr + (20 - (xr % 20));
    apple_y = yr + (20 - (yr % 20));
  }

    //set the privios direction
      previos_direction = direction

  //if player meets wall
  for (let step = 0; step < walls.length; step++) {
    if (direction == "u" && x == walls[step].x && y == walls[step].y + block_size) {
      direction = "stop";} 
    else if (direction == "d" && x == walls[step].x && y == walls[step].y - block_size) {
      direction = "stop";} 
    else if (direction == "l" && x == walls[step].x + block_size && y == walls[step].y) {
      direction = "stop";} 
    else if (direction == "r" && x == walls[step].x - block_size && y == walls[step].y) {
      direction = "stop";}
    // if (direction == previos_direction && x == walls[step].x - block_size && y == walls[step].y) {
    //   direction = "stop";}

  }

  ///puts the valeus of locatin and score in the html to show
  document.getElementById("x_value").innerHTML = x;
  document.getElementById("y_value").innerHTML = y;
  document.getElementById("score").innerHTML = score;

  //clean canvas
  ctx.drawImage(grass_img, 0, 0, 500, 500);

  //draw new player and apple

  if (direction == "r")ctx.drawImage(player_r, x, y, block_size, block_size);
  else if (direction == "l")ctx.drawImage(player_l, x, y, block_size, block_size);
  else if (direction == "u")ctx.drawImage(player_b, x, y, block_size, block_size);
  else if (direction == "d")ctx.drawImage(player_f, x, y, block_size, block_size);
  else if (direction == "stop")ctx.drawImage(player_s, x, y, block_size, block_size);

  // ctx.drawImage(player_img, x, y, block_size, block_size);
  // drow_player()
  ctx.drawImage(apple_img, apple_x, apple_y, block_size, block_size);

  // draw enemys and walls
  enemys();
  drow_walls();




  //only for dev use (F12)
  // console.log("score=" + score);
  // console.log("apple_x=" + apple_x);
  // console.log("apple_y=" + apple_y);
  //   console.log("random_num" + random_num)
  // console.log("wall" + walls);
  console.log(enemies)
}

//----------------------------------------------------
function key_strike() {
  // putting new valeus of player location
  if (event.keyCode == 40 && y < 480 && y >= 0) direction = "d";
  if (event.keyCode == 38 && y <= 480 && y > 0) direction = "u";
  if (event.keyCode == 37 && x <= 480 && x > 0) direction = "l";
  if (event.keyCode == 39 && x < 480 && x >= 0) direction = "r";
}


// function drow_player(){
//   ctx.drawImage(player_pics, x, y, block_size, block_size);  
//   }

// draw enemys
function enemys() {
  // ctx.drawImage(enemy_img, enemy_1x, enemy_1y, block_size, block_size);
  // ctx.drawImage(enemy_img, enemy_2x, enemy_2y, block_size, block_size);
  
  for (let i = 0; i < enemies.length; i++) {
    let enemy = enemies[i];
    ctx.drawImage(enemy_img, enemy.enemy_x, enemy.enemy_y, block_size, block_size);
  }
  
}


function drow_walls() {
  // for (let step = 0; step < screen[step]; step++) {
  //   ctx.drawImage(brick_img,screen[step],screen[step],block_size,block_size);}

    for (var i = 0; i < walls.length; i++)
  ctx.drawImage(brick_img, walls[i].x, walls[i].y, block_size, block_size);  
}

//----------------------------------------------------
///puts the canvas in the html to show
canvas = document.getElementById("myCanvas");
ctx = canvas.getContext("2d");

//declars var of player and puting in start pesition

var screen =  Array(0,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,1,0,0,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,0,0,
                    1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,
                    1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                    1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0);


walls = new Array();

//drows screen with matrix
screen_x = 0;
screen_y = 0;
for (var i = 0; i < screen.length; i++) {
  if (screen[i] == 1) {
    screen_x = i % 25;
    screen_y = Math.floor(i / 25);
    walls.push({ x:screen_x * 20, y: screen_y * 20 });
  }
}

var x = 40;
var y = 40;

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

var grass_img = new Image();
grass_img.src = "grass.jpg";

var brick_img = new Image();
brick_img.src = "brick.png";

var enemy_img = new Image();
enemy_img.src = "pics/enemy3.png";

var apple_img = new Image();
apple_img.src = "pics/seed.webp";

var portal_img = new Image();
portal_img.src = "pics/portal_side.webp";



//putts apple in random location
var xr = Math.floor(Math.random() * 480);
var yr = Math.floor(Math.random() * 480);
var apple_x = xr + (20 - (xr % 20));
var apple_y = yr + (20 - (yr % 20));

// putts enemys in random location


function random_num(){
  return Math.floor(Math.random() * 25) * 20;
}

// enemy 3
enemies = new Array();

// var enemy_x_location = Math.floor(Math.random() * 480);
// var enemy_y_location = Math.floor(Math.random() * 480);

enemy_3 = {
  enemy_x: random_num() + (20 - (random_num() % 20)),
  enemy_y: random_num() + (20 - (random_num() % 20)),
};

enemy_4 = {
  enemy_x: random_num() + (20 - (random_num() % 20)),
  enemy_y: random_num() + (20 - (random_num() % 20)),
};

enemies.push(enemy_3, enemy_4);




// // enemy 1
// var e1_xr = Math.floor(Math.random() * 480);
// var e1_yr = Math.floor(Math.random() * 480);
// var enemy_1x = e1_xr + (20 - (e1_xr % 20));
// var enemy_1y = e1_yr + (20 - (e1_yr % 20));
// // enemy 2
// var e2_xr = Math.floor(Math.random() * 480);
// var e2_yr = Math.floor(Math.random() * 480);
// var enemy_2x = e2_xr + (20 - (e2_xr % 20));
// var enemy_2y = e2_yr + (20 - (e2_yr % 20));

var previos_direction = 0;
var score = 0;
var block_size = 20;
var direction = "r";


// function random_num():
//   return Math.floor(Math.random() * 25)*20
//!!!!!!!!!!!!!!!!!!

//calls script
document.onkeydown = key_strike;
// constent movment
time = 200;
setInterval(game_play, time);
