class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r, maxLeft, maxRight = 0, len(height)-1, height[0], height[len(height)-1]
        total = 0
        while l < r:
            if(maxLeft < maxRight):
                l+=1
                maxLeft = max(maxLeft, height[l])
                total += maxLeft - height[l]
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                total += maxRight - height[r]
        return total
            
# so basically think of it like this, we move from the left side and right side
# think of us moving from the left side and right, but focus on the left for now
# so essentially, at position we know the maxLeft so far and the maxRight on the other side
# we move in the direction where maxLeft is smaller since thats the bottleneck, increasing it will
# essentially make the other max(maxRight in this case) the bottle neck!
# 2 sides and we go towards the middle from each as rainwater flows in from both sides and 
# we move inwards to increase the bottleneck. at ANY position, whether ur looking from the left or
# the right, it depends on the smaller max so just cause something ahead is gonna be more bigger
# so far that position has seen the smaller max SO FAR. for any position too, if its the new max,
# the calculation will come to 0. try to mentally visdualize it


#read this gpt explanation

# GOOD.
# This is actually a very honest and important stage in learning algorithms.

# You logically accept it…
# but your brain can’t “see the movie” yet.

# So let’s build the movie 🎬
# No formulas. Just a physical story.

# 🌧️ Imagine real terrain + rising water

# Picture the bars as real ground.

# You are controlling two giant sliding glass walls:

# one starts at the far left
# one starts at the far right

# They slowly move inward.

# Water is being poured into the terrain.

# ⭐ What the walls represent
# Left wall height = leftMax
# Right wall height = rightMax

# At the start:

# left wall height = height of first bar
# right wall height = height of last bar

# Because that’s all the terrain you have “locked in” so far.

# Everything inside is still unknown jungle 🌴

# 🧠 Now the KEY visual rule

# Water level in the container is always limited by
# 👉 the shorter glass wall

# If:

# left wall = height 2  
# right wall = height 5

# Then water can only rise to level 2 near the left side.

# Even if right side later becomes height 100.

# So the region near the left wall is already decided.

# You can safely move the left wall inward.

# 🎬 Now imagine the algorithm as a movie

# Step 1
# Walls at edges.

# Step 2
# Compare wall heights.

# shorter wall side → move that wall inward
# update that wall’s height if terrain is taller

# As walls move inward:

# 👉 the container shape gradually becomes known
# 👉 water in processed region is finalized

# You never need future info because
# the opposite wall already guarantees a taller boundary.

# 🔥 The intuition sentence that usually makes it click

# We are not computing water for the “current bar globally”.
# We are finalizing water for the region that is already sealed by a shorter boundary.

# That’s the whole trick.

# 🪜 Tiny concrete visualization

# Terrain:

# 0 1 0 2 1 0 1 3 ...
# ^             ^
# L wall        R wall

# Initially:

# leftMax = 0
# rightMax = 1

# Left wall is shorter →
# so water near left side can never exceed 0 → safe → move left.

# Now left wall hits height 1 → container grows.

# Now compare again.

# This is like slowly discovering the container shape from outside inward.

# ⭐ Why prefix array feels easier

# Because prefix method is like:

# “Scan the whole map first, then pour water.”

# Two-pointer is like:

# “Pour water while exploring the map.”

# That is harder to visualize until you see the motion.

# If you want, I can now do the best possible next step:

# 👉 I will simulate pointer movement
# 👉 draw left wall height / right wall height / water gained

# After ~5 steps your brain usually goes
# “OH WTF THAT’S SO OBVIOUS.”

# Wanna do that simulation?
