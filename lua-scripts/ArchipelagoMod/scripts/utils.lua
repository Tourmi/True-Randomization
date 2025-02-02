function Hash(str)
    local h = 5381;

    for c in str:gmatch"." do
        h = ((h << 5) + h) + string.byte(c)
    end
    return h
end

function TableContains(table, value)
    for i = 1, #table do
        if (table[i] == value) then
            return true
        end
    end
    return false
end

function ModPrint(...)
    local param = tostring(...)
    if (...).ToString ~= nil then param = (...):ToString() end
    print("[ArchipelagoMod] " .. param .. "\n")
end
