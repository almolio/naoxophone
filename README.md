1. Speech and tactile human-robot interface, aruco marker detection (5 points).
• Speech recognition and generation
• Tactile interface
• Aruco marker detection
2. Autonomous grasping of the sticks (20 points).
• The sticks should be on the xylophone stick holders and NAO already positioned in front of
them. You should start by implementing a pre-grasp behavior. Hint: you can manually move
the robot to a set of desired poses and measure the corresponding sequence of joint angles
via an appropriate ROS topic. You can then simply have the robot re-execute the captured
sequence of joint angles... (5 points)
• Once in pre-grasp pose, use the Cartesian control API to fine-tune the grasp motion using
visual feedback. (10 points)
• Assess the grasp status autonomously (5 points)
3. Play single notes on Xylophone (10 points).
• Define robust note positions (5 points)
• Use cartesian control to play all possible single notes (5 points)
4. Play Melody of at least 20 notes (10 points).
• Define set of 3 melodies of at least 20 notes each (5points)
• Add varying timing between notes (5 points)
5. Select Song (5 points).
• Provide list of available Songs (3 points)
• Select song from predefined set, via touch buttons or keyboard (2 points)
6. Learn melody from watching a demonstration (40 points).
• Detect notes being played on xylophone using computer vision methods. Try to make the
approach robust even if the demonstration is played with faster speeds. (20 points)
• Detect timing between notes (10 points)
• Verify timing constraints (NAO is slow) and correct accordingly (5points)
• Assign name and store for playback request (5 points)
