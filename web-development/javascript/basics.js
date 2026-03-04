// ============================================================
// JavaScript Basics — Ayaan's Learning Notes
// Topics: Variables, Functions, Arrays, Loops, DOM
// ============================================================

// -------------------------------------------------------
// 1. VARIABLES
// -------------------------------------------------------

// const = fixed value (can't be reassigned)
const name = "Ayaan";
const language = "JavaScript";

// let = value that can change
let score = 0;
let isLoggedIn = false;

// Data types
const age = 18;              // Number
const greeting = "Hello!";  // String
const isStudent = true;      // Boolean
const nothing = null;        // Null (intentionally empty)
let notDefined;              // undefined (not yet set)

console.log(`My name is ${name} and I'm learning ${language}.`);

// -------------------------------------------------------
// 2. FUNCTIONS
// -------------------------------------------------------

// Function declaration
function greet(personName) {
  return `Hello, ${personName}! 👋`;
}

// Arrow function (modern syntax)
const add = (a, b) => a + b;

// Function with default parameter
const welcome = (user = "stranger") => `Welcome, ${user}!`;

console.log(greet("Ayaan"));
console.log(add(5, 3));
console.log(welcome());
console.log(welcome("Ayaan"));

// -------------------------------------------------------
// 3. ARRAYS
// -------------------------------------------------------

// Creating an array
const topics = ["HTML", "CSS", "JavaScript", "Python"];

// Accessing elements (zero-indexed)
console.log(topics[0]);  // "HTML"
console.log(topics[2]);  // "JavaScript"

// Array length
console.log(topics.length);  // 4

// Adding & removing elements
topics.push("React");      // Add to end
topics.unshift("Basics");  // Add to beginning
topics.pop();              // Remove from end

console.log(topics);

// Useful array methods
const numbers = [3, 1, 4, 1, 5, 9, 2, 6];

const doubled = numbers.map(n => n * 2);
const evens = numbers.filter(n => n % 2 === 0);
const sum = numbers.reduce((total, n) => total + n, 0);

console.log("Doubled:", doubled);
console.log("Evens:", evens);
console.log("Sum:", sum);

// -------------------------------------------------------
// 4. LOOPS
// -------------------------------------------------------

// For loop
for (let i = 0; i < topics.length; i++) {
  console.log(`Topic ${i + 1}: ${topics[i]}`);
}

// For...of loop (cleaner for arrays)
for (const topic of topics) {
  console.log(`Learning: ${topic}`);
}

// forEach method
topics.forEach((topic, index) => {
  console.log(`${index + 1}. ${topic}`);
});

// While loop
let countdown = 5;
while (countdown > 0) {
  console.log(`Countdown: ${countdown}`);
  countdown--;
}

// -------------------------------------------------------
// 5. OBJECTS
// -------------------------------------------------------

const student = {
  name: "Ayaan",
  age: 18,
  skills: ["HTML", "CSS", "JS"],
  isStudent: true,
  greet() {
    return `Hi, I'm ${this.name}!`;
  }
};

console.log(student.name);
console.log(student.greet());

// Destructuring
const { name: studentName, age: studentAge } = student;
console.log(studentName, studentAge);

// -------------------------------------------------------
// 6. CONDITIONALS
// -------------------------------------------------------

const userScore = 85;

if (userScore >= 90) {
  console.log("Grade: A 🌟");
} else if (userScore >= 75) {
  console.log("Grade: B 👍");
} else {
  console.log("Grade: C — keep going! 💪");
}

// Ternary operator (shorthand if/else)
const status = userScore >= 50 ? "Passed ✅" : "Failed ❌";
console.log(status);

// -------------------------------------------------------
// 7. DOM MANIPULATION
// (Run this in a browser, not Node.js)
// -------------------------------------------------------

/*
// Select an element
const heading = document.querySelector('h1');
const button = document.getElementById('myButton');

// Change content
heading.textContent = 'Hello, World!';
heading.style.color = '#6c63ff';

// Listen for events
button.addEventListener('click', () => {
  alert('Button clicked!');
  heading.textContent = 'You clicked the button! 🎉';
});

// Create and add elements dynamically
const newParagraph = document.createElement('p');
newParagraph.textContent = 'This paragraph was added with JavaScript!';
document.body.appendChild(newParagraph);
*/

// -------------------------------------------------------
// 8. USEFUL BUILT-IN METHODS
// -------------------------------------------------------

// String methods
const message = "  Hello, Ayaan!  ";
console.log(message.trim());           // Remove whitespace
console.log(message.toUpperCase());    // Uppercase
console.log(message.includes("Ayaan")); // Check substring
console.log(message.replace("Ayaan", "World")); // Replace

// Math methods
console.log(Math.max(1, 5, 3));        // 5
console.log(Math.min(1, 5, 3));        // 1
console.log(Math.floor(4.7));          // 4
console.log(Math.ceil(4.1));           // 5
console.log(Math.round(4.5));          // 5
console.log(Math.random());            // 0 to 1 (random)

// Random integer between min and max (inclusive)
const randomInt = (min, max) => Math.floor(Math.random() * (max - min + 1)) + min;
console.log(randomInt(1, 10));
