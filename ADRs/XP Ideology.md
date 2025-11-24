# Architecture Decision Record: XP Ideology and Distribution

## Context
As a TTRPG dungeon master (DM), I want to run a game using experience points (XP) that is not ONLY considering combat as a mechanic to provide players with XP, but considers social encounters, and generic situations, such as skill challenges, all under the category of an Encounter.  
Encounters shall be weighted as Easy, Moderate, Hard, or Impossible, with the DM able to adjust the XP that is offered for each of these encounter categories.  
Additionally we want to reward players for discoveries and growing discoveries aka LORE. 
Finally whether players finish side quests, or follow the plot, this should provide them some additional XP for their progress.

## Decision(s)
### Experience Points
Encounters (social, skill, or combat) with tiers: Easy < Moderate < Hard < Impossible  
Lore rewards where New Lore > Enhanced Lore, but not by a huge margin  
Plot-following as a small nudge.  
Side quests as a solid, static bonus per quest.

## Rationale
We will build out our XP to be adjustable/configurable by the DM, or whoever has the application, but will provide a 'baseline' XP distribution based on the ideology that a Moderate encounter is the most common present in our games, and increasing or decreasing based on this ideology.  
We should consider a 'scaling' factor for campaigns that are considered more on a harder or easier scale by the DM, but will look at that at a later enhancement.  

### Starting Baseline XP Values (Per Player, Per Session)
#### Encounters
Type	XP (each)	Notes  
Easy	50	A quick scene, almost no risk.  
Moderate	100	Baseline challenge – most fights / tense social scenes.  
Hard	150	Dangerous, resource-taxing; felt like a big deal.  
Impossible	225	“We probably shouldn’t win this” or huge boss / set-piece.  

#### Lore
Type	XP (each)	Notes  
Enhanced Lore	30	Deepening or connecting existing knowledge.  
New Lore	50	Genuinely new, meaningful piece of world or plot info.  

#### Questing
Type	XP	Notes  
Followed Plot	25 flat	A little “you’re steering with the story” treat.  
Completed Side Quest 100 (each) significant but not dominant.  

## Conclusion
This setup provides a quick starting state for our tool, but also allows the DMs the ability to adjust the values as they see fit.
