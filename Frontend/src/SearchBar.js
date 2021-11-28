import React from "react";

class SearchBar extends React.Component {
  state = { term: "" };
  onSubmitQuery = (event) => {
    event.preventDefault();
    this.props.onFormSubmit(this.state.term);
    // console.log(this.state.term);
  };

  render() {
    return (
      <div className="search-bar ui segment">
        <form className="ui form" onSubmit={this.onSubmitQuery}>
          <div className="field">
            <label>Search The Conference Here...</label>
            <input
              type="text"
              value={this.state.term}
              onChange={(e) => {
                this.setState({ term: e.target.value });
              }}
            />
          </div>
        </form>
      </div>
    );
  }
}
export default SearchBar;
