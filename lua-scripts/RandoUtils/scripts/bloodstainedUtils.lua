function ValidUObjectOrNil(uObject)
    if uObject ~= nil and uObject:IsValid() then return uObject end
    return nil
end

local gameInstanceCache
---@return UPBGameInstance, string?
function GetGameInstance()
    if ValidUObjectOrNil(gameInstanceCache) == nil then
        ---@type UPBGameInstance?
        gameInstanceCache = ValidUObjectOrNil(FindFirstOf("PBGameInstance"))
    end

    if gameInstanceCache == nil or not gameInstanceCache:IsValid() then
        return gameInstanceCache, "GameInstance is invalid"
    end

    return gameInstanceCache, nil
end
