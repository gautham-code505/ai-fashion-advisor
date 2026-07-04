# LARA Testing & Verification Guide

This document outlines the final test cases executed on the LARA AI Fashion Advisor to ensure all features work correctly before submission.

## 1. UI & Responsiveness Testing
| Feature | Expected Behavior | Status |
|---|---|---|
| **Form Loading State** | Upon submitting the form, the button disables, dims, and displays "LARA is curating your perfect look..." with a spinner. | ✅ Pass |
| **Mobile Navigation** | The hamburger menu opens/closes correctly. The "Clear Saved Looks" option appears at the bottom of the mobile menu if looks are saved. | ✅ Pass |
| **Responsive Grid** | The recommendation cards stack in a single column on mobile screens and expand to a 2/3 column layout on desktop. | ✅ Pass |

## 2. Core Recommendation Engine Testing
| Feature | Expected Behavior | Status |
|---|---|---|
| **Exact Match** | Submitting standard preferences (e.g., Women, Party, Hourglass, 5000 budget) returns a complete 3-piece outfit under 5000 INR. | ✅ Pass |
| **No-Results State** | If preferences are too narrow and yield 0 products, the app does not crash. It displays a "No exact matches found" card suggesting new parameters. | ✅ Pass |
| **Budget Logic** | The engine iteratively adds items, ensuring the `total_price` never exceeds the selected `budget` tier. | ✅ Pass |

## 3. Gemini AI Integration (Resiliency Testing)
| Scenario | Expected Behavior | Status |
|---|---|---|
| **No `.env` file** | Application loads safely. The local text generator provides a fallback message. "Personalized by LARA" badge is hidden. | ✅ Pass |
| **Invalid API Key** | Application catches the `google-generativeai` exception. Falls back gracefully to local text without crashing the server. | ✅ Pass |
| **`USE_GEMINI=False`** | Bypasses the API call entirely. Uses local text generator. | ✅ Pass |
| **Valid API Key** | Generates a <90 word message summarizing the outfit. "Personalized by LARA" badge is visible on the results page. | ✅ Pass |

## 4. LocalStorage (Save This Look) Testing
| Scenario | Expected Behavior | Status |
|---|---|---|
| **Save Look** | Clicking "Save This Look" changes the button to "Saved ✓", shows a toast notification, and increments the navbar badge. | ✅ Pass |
| **Page Refresh** | Reloading the results page persists the "Saved ✓" button state and the navbar badge count using `localStorage`. | ✅ Pass |
| **Duplicate Prevention** | Clicking the button multiple times does not increment the badge or add duplicate keys to `localStorage`. | ✅ Pass |
| **Clear Looks** | Clicking "Clear saved looks" in the navbar/mobile menu removes the `localStorage` key, resets the badge to 0, and reverts the button text. | ✅ Pass |
