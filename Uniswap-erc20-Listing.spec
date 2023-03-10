/*
    This is a specification file for the verification of ERC20s
    smart contract using the Certora prover. */
 //                                Methods                                 //
////////////////////////////////////////////////////////////////////////////
/*
    Declaration of methods that are used in the rules. envfree indicate that
    the method is not dependent on the environment (msg.value, msg.sender).
    Methods that are not declared here are assumed to be dependent on env.
*/
        methods {
    totalSupply()                         returns (uint256)   envfree
    balanceOf(address)                    returns (uint256)   envfree
    allowance(address,address)            returns (uint256)   envfree
    increaseAllowance(address, uint256)
    decreaseAllowance(address, uint256)
    transfer(address,uint256)
    transferFrom(address,address,uint256)
    mint(address,uint256)
    burn(uint256)
    burnFrom(address,uint256)
    initialize(address)
    delegates(address)                    returns (address) envfree
    getVotes(address)                     returns (uint256) envfree
}
      definition MAX_SUPPLY() returns uint256 = 4294967296;
      function doesntChangeBalance(method f) returns bool {
    return f.selector != transfer(address,uint256).selector &&
        f.selector != transferFrom(address,address,uint256).selector &&
        f.selector != mint(address,uint256).selector &&
        f.selector != burn(uint256).selector &&
        f.selector != burnFrom(address,uint256).selector &&
        f.selector != initialize(address).selector;
}
      
     
