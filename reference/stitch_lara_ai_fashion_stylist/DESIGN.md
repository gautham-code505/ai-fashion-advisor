---
name: Premium AI Fashion Advisor
colors:
  surface: '#faf9f7'
  surface-dim: '#dadad8'
  surface-bright: '#faf9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeec'
  surface-container-high: '#e9e8e6'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1b'
  on-surface-variant: '#47464c'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#78767d'
  outline-variant: '#c8c5cd'
  surface-tint: '#5d5c74'
  primary: '#00000b'
  on-primary: '#ffffff'
  primary-container: '#1a1a2e'
  on-primary-container: '#83829b'
  inverse-primary: '#c6c4df'
  secondary: '#67558d'
  on-secondary: '#ffffff'
  secondary-container: '#d5bfff'
  on-secondary-container: '#5d4a82'
  tertiary: '#010000'
  on-tertiary: '#ffffff'
  tertiary-container: '#231a0c'
  on-tertiary-container: '#91826d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e0fc'
  primary-fixed-dim: '#c6c4df'
  on-primary-fixed: '#1a1a2e'
  on-primary-fixed-variant: '#45455b'
  secondary-fixed: '#ebddff'
  secondary-fixed-dim: '#d2bcfc'
  on-secondary-fixed: '#230f45'
  on-secondary-fixed-variant: '#4f3d73'
  tertiary-fixed: '#f2e0c8'
  tertiary-fixed-dim: '#d6c4ad'
  on-tertiary-fixed: '#231a0c'
  on-tertiary-fixed-variant: '#514534'
  background: '#faf9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e3e2e0'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  container-max: 1440px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  unit-xs: 4px
  unit-sm: 8px
  unit-md: 16px
  unit-lg: 24px
  unit-xl: 48px
---

## Brand & Style
The design system embodies a "Contemporary Heritage" aesthetic—fusing the precision of high-end technology with the warmth of Indian luxury. It targets a fashion-forward audience that values curated discovery over bulk browsing. 

The style is **Minimal-Premium**. It borrows the spaciousness and structural discipline of Apple’s interface design while integrating the dense product information architecture common in top-tier e-commerce. The emotional response should be one of "effortless sophistication": the UI feels invisible until needed, allowing high-resolution editorial photography and AI-driven recommendations to take center stage.

## Colors
The palette is rooted in a soft, non-clinical foundation.
- **Base:** The primary background uses a soft cream (#F9F8F6) rather than pure white to evoke a tactile, premium paper feel.
- **Accents:** Deep Navy (#1A1A2E) provides authoritative contrast for navigation and primary actions. Subtle Purple (#8E7AB5) is used sparingly for AI-enhanced features or special tags.
- **Gradients:** Use a soft linear gradient between the Purple and Warm Beige (#DDCBB4) at low opacity (10-15%) for AI interaction containers to distinguish them from standard commerce modules.
- **Functional:** Success, error, and warning states should be slightly desaturated to maintain the sophisticated mood.

## Typography
The system employs a dual-font strategy. **Montserrat** is used for headlines to provide a bold, geometric confidence that feels modern and architectural. **Inter** is used for all body text, metadata, and labels to ensure maximum legibility at smaller scales, particularly for product descriptions and pricing. 

Use wide letter-spacing on `label-md` for secondary navigation and category tags to reinforce the editorial look. Display sizes should utilize tighter tracking for a high-impact, "magazine cover" feel.

## Layout & Spacing
This design system utilizes a **Fixed Grid** approach for desktop (12 columns) and a **Fluid Grid** for mobile (4 columns). 

- **Vertical Rhythm:** Built on an 8px base unit. 
- **Whitespace:** Emphasize generous vertical margins (`unit-xl`) between sections to prevent the UI from feeling cluttered, mimicking luxury retail store layouts.
- **Mobile:** Transition to tighter gutters (`16px`) but maintain the large side margins (`20px`) to ensure the "premium" feel is not lost on smaller screens.
- **Product Grids:** On desktop, use a 3 or 4-column layout for products to allow the imagery enough room to breathe.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** and **Tonal Layers**. 
- **Shadows:** Use extremely soft, large-radius shadows (e.g., `box-shadow: 0 10px 40px rgba(26, 26, 46, 0.04)`). Shadows should feel like light catching the edge of a physical card rather than a floating element.
- **Layers:** Use the Tertiary Beige (#DDCBB4) at very low opacities (5-8%) for "sunken" containers like search bars or filter backgrounds.
- **AI Components:** Utilize a subtle backdrop-blur (Glassmorphism) with the purple/beige gradient for the AI chat interface to denote a "smarter" layer existing above the standard commerce plane.

## Shapes
The shape language is defined by significant corner rounding to evoke friendliness and modern tech. 
- **Cards:** Product cards must use `rounded-xl` (24px) to create a soft, high-end look.
- **Buttons:** Primary buttons should use the same `rounded-xl` or be fully pill-shaped to stand out against the structured grid.
- **Inputs:** Use `rounded-lg` (16px) for form fields to maintain consistency without appearing overly "bubbly."

## Components
- **Buttons:** Primary buttons are Solid Navy (#1A1A2E) with white text. Secondary buttons use a Navy outline with a subtle hover fill. 
- **AI Chat Bubble:** Features a gradient border (Purple to Beige) and a backdrop blur effect. The typography inside is Inter 16px.
- **Product Cards:** No visible borders. Use the ambient shadow and the Soft Cream background. The image should be the hero, with text (Price and Title) left-aligned using Inter.
- **Chips:** Used for sizing and categories. Pill-shaped, using the Warm Beige as a background for selected states and a thin 1px Navy border for unselected.
- **Navigation:** Top-tier navigation is minimal. Use thin icons and Montserrat 14px uppercase labels. 
- **Input Fields:** Floating labels with a light Tertiary Beige background and a subtle transition to a Purple border on focus to signal "AI-readiness."