
    class ListItem extends React.Component {
      state = {show:false}

      onToggleView = () => {
        this.setState({ show: (this.state.show == true) ? false : true });
      }

      render() {
        return (
          <li>
            <div>
              <span className='green-highlight'>Key:</span>
              <span> {this.props.item.key} </span>

              <input
                type="button"
                value= {this.state.show ? " hide value " : " show value " }
                onClick={this.onToggleView}
              />
            </div>

            { this.state.show ? <div><span className='green-highlight'>Value:</span>
            <span> {this.props.item.value} </span></div> : null }

          </li>
        );
      }
    }

    class List extends React.Component {
      state = {}

      componentDidMount () {
        fetch('json')
          .then(res => res.json())
          .then(this.onLoad);
      }

      onLoad = (data) => {
        this.setState({
          data: data
        });
      }

      render () {
        const { data } = this.state;

        return data ?
          this.renderData(data) :
          this.renderLoading()
      }

      renderListItem = item =>
        <ListItem key={item.key} item={item} />;

      renderData (data) {
        if (data && data.length) {
          return (
            <div>
              <h2>Stored Data:</h2>
              <ul>
                {this.state.data.map(this.renderListItem)}
              </ul>
            </div>
          );
        } else {
          return <div className="message">No items found</div>
        }
      }

      renderLoading () {
        return <div className="message">Loading...</div>
      }
    }
