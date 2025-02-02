require("utils")
require("UEHelpers")

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

    return gameInstanceCache
end

local characterInventoryCache
---@return UPBCharacterInventoryComponent, string?
function GetInventory()
    if ValidUObjectOrNil(characterInventoryCache) == nil then
        ---@type UPBCharacterInventoryComponent?
        characterInventoryCache = ValidUObjectOrNil(FindFirstOf("PBCharacterInventoryComponent"))
    end
    if characterInventoryCache == nil or not characterInventoryCache:IsValid() then
        return characterInventoryCache, "Character inventory was invalid"
    end
    return characterInventoryCache
end

---@param message string
---@param duration number
function MessagePlayer(message, duration)
    if duration == nil then duration = 5 end
    local gameInstance = GetGameInstance()
    gameInstance:OCMsg(message, duration)
    ModPrint("Message: " .. message)
end

---@param itemName string
---@param quantity number
---@return string?
function GiveItem(itemName, quantity)
    ExecuteInGameThread(function()
        local characterInventory, error = GetInventory()
        if error ~= nil then
            ModPrint("Error while giving item: " .. error)
        end

        characterInventory:GetItemWithDisplay(FName(itemName), quantity, true)
    end)
end

function KillPlayer(message)
    MessagePlayer(message, 5)
    GetGameInstance():GetPlayerCharacter(0):Kill()
end
