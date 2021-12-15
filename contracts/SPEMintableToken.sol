// SPDX-License-Identifier: MIT
pragma solidity 0.8.0;

import "@openzeppelin/contracts/token/ERC20/presets/ERC20PresetMinterPauser.sol";

contract SPEMintableToken is ERC20PresetMinterPauser {
    constructor(uint256 initialSupply)
        ERC20PresetMinterPauser("Space Energy", "SPE")
    {
        _mint(msg.sender, initialSupply);
    }
}
