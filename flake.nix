{
  description = "Simple Todoist task adder";

  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-23.11";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
    poetry2nix,
  }:
    flake-utils.lib.eachDefaultSystem (system: let
      # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
      pkgs = nixpkgs.legacyPackages.${system};
      inherit (poetry2nix.lib.mkPoetry2Nix {inherit pkgs;}) mkPoetryApplication;
      inherit (pkgs) writeShellScriptBin;
    in {
      packages = {
        todoister = mkPoetryApplication {
          projectDir = ./.;
          preferWheels = true;
        };
        wofi-todo = writeShellScriptBin "wofi-todo.sh" ''
          chosen=$(${pkgs.xclip}/bin/xclip -o -selection clipboard | ${pkgs.wofi}/bin/wofi --dmenu --gtk-dark -l 1 -p "Add todo")
          ${self.packages.${system}.todoister}/bin/todoister --notify false "$chosen"
        '';
        default = self.packages.${system}.todoister;
      };

      devShells.default = pkgs.mkShell {
        inputsFrom = [self.packages.${system}.todoister];
        packages = [pkgs.poetry pkgs.ruff];
      };
    });
}
