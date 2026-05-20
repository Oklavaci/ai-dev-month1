# 🎮 Arm Control Game - Network Latency Challenge

An interactive web-based game where you control a robotic arm positioned on the ground to catch a moving object, but with **100ms network latency** simulating real-world network ping delays.

## 🎯 Game Objective

- Use **left/right arrow keys** to position the arm horizontally
- Press **down arrow** to extend the arm and catch the moving object
- Account for the **100ms delay** between your input and the arm's response
- Beat your catch rate!

## 🕹️ Controls

| Key | Action |
|-----|--------|
| `←` `→` | Move arm left/right |
| `↓` | Extend arm to catch object |

## ⚙️ Game Mechanics

### Network Latency Simulation
- Every key press is **delayed by 100ms** before the arm responds
- You can see the input queue in the top-left corner showing pending inputs
- You must **predict** where the object will be and position preemptively

### Object Movement
- The green ball bounces continuously on the ground
- Moves in **longer streaks** (not rapid bouncing) making patterns predictable
- Smooth motion allows you to anticipate its path
- Physics include gravity, bounce, and friction
- Directional changes happen every 60-140 frames for natural movement

### Arm Control
- Horizontal arm positioned on the ground
- Smooth left/right movement via arrow keys
- Down arrow extends the arm to catch the object
- Catch happens when arm is fully extended and near the ball
- Red color indicates catch zone

### Scoring
- **Caught Objects**: Number of successful catches
- **Attempts**: Number of times the object falls off-screen
- **Catch Rate**: Percentage of objects caught
- **Ping Delay**: Always 100ms to simulate network conditions

## 🎮 How to Play

1. Open `index.html` in any modern web browser
2. Watch the green ball bouncing on the ground
3. **Position** the arm with ← and → keys to intercept the ball's path
4. **Time** your press of the ↓ key to catch as the ball passes through
5. **Remember**: Your inputs are delayed by 100ms, so act 100ms early!
6. Click "Reset Game" to restart

## 💡 Tips & Tricks

1. **Predict Motion**: The object moves in predictable streaks, not randomly
2. **Early Position**: Move the arm AHEAD of where the ball is moving
3. **Timing is Key**: The down arrow must be pressed slightly before the ball arrives
4. **Account for Delay**: Everything you do is 100ms behind what you see
5. **Practice**: You'll improve as you learn the ball's bounce patterns

## 📊 Performance Metrics

- **Real-time Statistics**: Track your progress with live catch rate
- **Input Queue Status**: See exactly how many ms until your inputs execute
- **Visual Feedback**: Get instant confirmation when you catch an object

## 🖥️ Technical Features

- **Canvas-based Rendering**: Smooth 60 FPS animation
- **Physics Engine**: Gravity, bounce, friction, and collision detection
- **Input Queue System**: Realistic network latency simulation
- **Responsive Design**: Works on different screen sizes
- **No Dependencies**: Pure HTML/CSS/JavaScript

## 🧪 Browser Compatibility

Works on all modern browsers:
- Chrome/Chromium
- Firefox
- Safari
- Edge

## 🔧 Customization

You can modify these parameters in the JavaScript:

```javascript
const INPUT_DELAY = 100;        // Change network latency (ms)
arm.catchRadius = 50;           // Catch zone radius
arm.maxExtend = 80;             // How far arm extends
object.gravity = 0.2;           // Gravity strength
```

## 📝 Game State

The game continuously tracks:
- Caught objects
- Total attempts
- Catch percentage
- Pending input queue

---

**Enjoy the challenge! How high can you get your catch rate? 🚀**
