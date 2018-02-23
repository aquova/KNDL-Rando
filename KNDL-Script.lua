-- This is a script to randomize Kirby's ability in Kirby: Nightmare in Dreamland
-- To be used with the Lua-compatible emulator and a US ROM of K.N.D.
-- Written by Austin Bricker (Aquova), 2017

-- The power in Kirby's mouth is stored in 0x217A
address = 0x217B

-- These are the valid values for Kirby abilities, including no ability
abilities = {0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0A, 0x0B, 0x0C, 0x0D, 0x0E, 0x0F, 0x10, 0x11, 0x12, 0x13, 0x14, 0x15, 0x16, 0x17, 0x18}

-- Function that chooses a random ability when called
function rand_kirby(a)
    val = math.random(0,#a - 1)
    return a[val]
end

prev_mouth = 0x00 -- If nothing in Kirby's mouth, defaults to 0x00
while true do
    mouth = memory.readbyte(address) -- Read what's currently in mouth
    if mouth ~= prev_mouth and mouth ~= 0x00 then
        next_ability = rand_kirby(abilities) -- Chooses new ability
        memory.writebyte(address, next_ability) -- Replaces old mouth content
        prev_mouth = next_ability
    end
    emu.frameadvance()
end
